import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ------------------------------
# Check if a matrix is balanced
# ------------------------------
def is_balanced(matrix):
    """
    Check if a given matrix is balanced (all row and column sums are equal).

    Args:
        matrix (pd.DataFrame): A matrix of edge weights.

    Returns:
        bool: True if all rows and columns sum to the same value (within tolerance), else False.

    Examples:
        >>> m = pd.DataFrame({
        ...     'Item 1': [0.5, 0.5],
        ...     'Item 2': [0.5, 0.5]
        ... }, index=['Player 1', 'Player 2'])
        >>> is_balanced(m)
        True
    """
    row_sums = matrix.sum(axis=1)
    col_sums = matrix.sum(axis=0)
    target = round(row_sums.iloc[0], 5)
    return all(abs(val - target) < 1e-5 for val in row_sums) and all(abs(val - target) < 1e-5 for val in col_sums)

# ---------------------------------------------------
# Perform Birkhoff decomposition on a balanced matrix
# ---------------------------------------------------
def birkhoff_algorithm(weight_matrix, verbose=True):
    """
    Perform Birkhoff decomposition on a balanced weight matrix.

    Args:
        weight_matrix (pd.DataFrame): Matrix representing a bipartite graph with edge weights.
        verbose (bool): If True, prints steps and shows graphs.

    Returns:
        list: List of matchings (each matching is a list of tuples (i, j))
        list: List of corresponding probabilities (minimum weight in each matching)
        list: List of intermediate matrix states (after each iteration)

    The algorithm repeatedly finds a perfect matching with positive weights,
    subtracts the minimal weight in that matching, and continues until the graph is empty.

    If the input matrix is not balanced, the function will return empty results.
    """
    if not is_balanced(weight_matrix):
        if verbose:
            print("Error: Input matrix is not balanced. Birkhoff decomposition is only valid for balanced matrices.")
        return [], [], []

    steps = []
    matrix = weight_matrix.copy()
    matchings = []
    probabilities = []
    step_number = 1

    while True:
        if verbose:
            print(f"\nStep {step_number}:")
        G = nx.Graph()
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                w = matrix.iat[i, j] # Get the weight of the edge in numerical form
                if pd.notna(w) and w > 0:
                    G.add_edge(f"Player {i+1}", f"Item {j+1}", weight=w)

        # Find maximum weight matching
        matching = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)

        if len(matching) < rows:
            if verbose:
                print("\nAlgorithm failed - no more perfect matching found.")
            break

        # Convert matching to a list of tuples (i, j)
        current_matching = []
        for u, v in matching:
            if "Player" in u:
                i = int(u.split()[1]) - 1
                j = int(v.split()[1]) - 1
            else:
                i = int(v.split()[1]) - 1
                j = int(u.split()[1]) - 1
            current_matching.append((i, j))

        # Calculate the minimum edge weight in the current matching
        min_weight = min(matrix.iat[i, j] for i, j in current_matching)
        if verbose:
            print(f"Matching: {[(f'Player {i+1}', f'Item {j+1}') for i, j in current_matching]}")
            print(f"Minimum edge weight: {min_weight}")

        for i, j in current_matching:
            matrix.iat[i, j] -= min_weight
            if matrix.iat[i, j] == 0:
                matrix.iat[i, j] = np.nan

        matchings.append(current_matching)
        probabilities.append(float(min_weight))
        steps.append(matrix.copy())

        if verbose:
            display_matrix(matrix, step_number)
            draw_graph(matrix, step_number)

        step_number += 1

    return matchings, probabilities, steps

# ----------------------------
# Draw the bipartite graph
# ----------------------------
def draw_graph(matrix, step_number):
    """
    Visualizes the current graph without edge weights.
    """
    G = nx.Graph()
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if pd.notna(matrix.iat[i, j]) and matrix.iat[i, j] > 0:
                G.add_edge(f"Player {i+1}", f"Item {j+1}")

    pos = {}
    for i in range(rows):
        pos[f"Player {i+1}"] = (0, -i)
    for j in range(cols):
        pos[f"Item {j+1}"] = (1, -j)

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    plt.title(f"Step {step_number} - Graph")
    plt.axis('off')
    plt.show()

# ----------------------------
# Display matrix in terminal
# ----------------------------
def display_matrix(matrix, step_number):
    """
    Prints the weight matrix after each step.
    """
    print(f"\nWeight matrix after step {step_number}:")
    display_df = matrix.copy()
    display_df.index.name = "Players"
    display_df.columns.name = "Items"
    print(display_df.fillna(0).round(2))

# ----------------------------
# Example run + doctest trigger
# ----------------------------
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    weights = pd.DataFrame({
        'Item 1':   [0.3, 0.3, 0.4, 0.0],
        'Item 2':   [0.3, 0.0, 0.4, 0.3],
        'Item 3': [0.0, 0.3, 0.2, 0.5],
        'Item 4':   [0.4, 0.4, 0.0, 0.2]
    }, index=['Player A', "Player B", "Player C", 'Player D'])

    matchings, probs, steps = birkhoff_algorithm(weights)
