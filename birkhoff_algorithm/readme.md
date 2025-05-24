## 🧮 Birkhoff Decomposition Algorithm

This Python implementation provides a complete solution for performing the **Birkhoff–von Neumann decomposition** of a doubly stochastic matrix, using matchings in bipartite graphs.

### 📌 What it does

* Accepts a **balanced** matrix representing weights between two sets (players and items).
* Iteratively finds **perfect matchings** and **decomposes** the matrix into a convex combination of permutation matrices.
* Visualizes each step of the decomposition using **networkx** and **matplotlib**.
* Supports internal testing via `doctest`.

---

### 🚀 How to Run

Make sure to install dependencies:

```bash
pip install pandas matplotlib networkx
```

Then execute:

```bash
python birknhof.py
```

You will see:

* Step-by-step matchings
* Weight reduction in the matrix
* Graph visualization (one per step)

---

### 💪 Running Tests

To run internal `doctest` validation:

```bash
python birknhof.py
```

The tests will be triggered automatically from within the `__main__` section.

---

### 📚 Files

* **birknhof.py** — Main script containing all functions:

  * `is_balanced()` – checks if matrix is balanced
  * `birkhoff_algorithm()` – performs the decomposition
  * `draw_graph()` – visualizes each step as a bipartite graph
  * `display_matrix()` – prints the current matrix

---

### 🧠 Notes

* Only works correctly on **balanced** matrices (i.e., all rows and columns sum to the same value).
* If the matrix is not balanced, the function exits gracefully with a warning.
* The algorithm terminates when no more perfect matching exists.
