import matplotlib.pyplot as plt
import random
import time
from collections import deque
from typing import List, Tuple


def egalitarian_allocation_sorted_pruning(valuations: List[List[int]], print_result=True) -> List[List[int]]:
    """
    אלגוריתם אגליטרי עם גיזום לפי מצבים שקולים – וקטור סכומים ממוין.
    """
    num_players = len(valuations)
    num_items = len(valuations[0])
    best_allocation = None
    best_min_value = float('-inf')
    best_sums = None

    initial_state = (0,) * num_players + (0,)
    queue = deque()
    queue.append((initial_state, [[] for _ in range(num_players)]))

    visited = set()
    # במקום לשמור את הסכומים עצמם, נשמור את הסכומים אחרי מיון + אינדקס חפצים
    visited.add(tuple(sorted(initial_state[:num_players])) + (0,))

    while queue:
        state, allocation = queue.popleft()
        current_sums = state[:num_players]
        current_index = state[num_players]

        if current_index == num_items:
            min_val = min(current_sums)
            if (
                min_val > best_min_value or
                (min_val == best_min_value and (best_sums is None or sorted(current_sums) > sorted(best_sums)))
            ):
                best_min_value = min_val
                best_allocation = allocation
                best_sums = current_sums
            continue

        pessimistic_bound = best_min_value
        optimistic_values = [
            current_sums[i] + sum(valuations[i][j] for j in range(current_index, num_items))
            for i in range(num_players)
        ]
        optimistic_bound = min(optimistic_values)
        if optimistic_bound < pessimistic_bound:
            continue

        for i in range(num_players):
            new_sums = list(current_sums)
            new_sums[i] += valuations[i][current_index]
            new_state = tuple(new_sums) + (current_index + 1,)

            # גיזום לפי סכומים ממוין
            visited_key = tuple(sorted(new_sums)) + (current_index + 1,)
            if visited_key in visited:
                continue
            visited.add(visited_key)

            new_allocation = [list(items) for items in allocation]
            new_allocation[i].append(current_index)
            queue.append((new_state, new_allocation))

    if print_result:
        for player, items in enumerate(best_allocation):
            value = sum(valuations[player][item] for item in items)
            print(f"Player {player} gets items {items} with value {value}")

    return best_allocation


def run_time_test_with_graph():
    item_counts = list(range(1, 10))
    player_counts = [2, 3, 4]

    for num_players in player_counts:
        times = []
        for num_items in item_counts:
            valuations = [
                [random.randint(1, 2 ** 32) for _ in range(num_items)]
                for _ in range(num_players)
            ]
            start = time.time()
            egalitarian_allocation_sorted_pruning(valuations, print_result=False)
            end = time.time()
            times.append((end - start) * 1000)  # ms

        plt.figure()
        plt.plot(item_counts, times, marker='o')
        plt.title(f"Execution Time - Sorted Sum Pruning - {num_players} Players")
        plt.xlabel("Number of Items")
        plt.ylabel("Execution Time (ms)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    run_time_test_with_graph()
    # valuations = [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]]
    # best_allocation = egalitarian_allocation_sorted_pruning(valuations, print_result=False)
    # for player, items in enumerate(best_allocation):
    #     value = sum(valuations[player][item] for item in items)
    #     print(f"Player {player} gets items {items} with value {value}")