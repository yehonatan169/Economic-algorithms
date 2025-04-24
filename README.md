# Egalitarian Allocation - Fair Division with Pruning

This project implements an **exact and optimal algorithm** for solving the **Egalitarian Allocation problem** — fairly dividing indivisible goods between players, while maximizing the value of the **least satisfied player**.

---

## 📚 Project Overview

### ✨ Goal
Given:
- A matrix of valuations (each row = one player's values for items),
- An integer number of items and players,

Find:
- A partition of the items such that the **minimum value** received by any player is **maximized** (Egalitarian fairness).

---

## 🧩 Structure



---

## ✅ Section A – Exact Algorithm + State Space Search

### Approach:
We explore the **entire allocation tree**, where each level corresponds to assigning one item to some player.

### Optimizations:
- **Pruning A**: Skip states we have already visited (same values for all players and same index).
- **Pruning B**: Calculate an optimistic bound for the current path. If it cannot surpass the best minimum value so far — stop.

### Example:
For `valuations = [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]]`, the algorithm explores all possible item assignments and returns:



This is the **most egalitarian** split (min value = 15).

---

## 📊 Section B – Runtime Analysis

We tested the algorithm for various:
- Number of items (1 to 10),
- Number of players (2, 3, 4),
- **Valuations = Random integers in [1, 2^32]**.

### Graphs:
We measured execution time (ms) per configuration and plotted:

- `Execution Time vs Number of Items`
- One plot per player count
- Using `matplotlib`

This provided insight into how runtime grows **exponentially** with item count.

---

## 🚀 Section G – Improved Pruning Rules (Advanced)

We developed new pruning ideas to speed up search **without compromising optimality**:

### ✅ Sorted Sums Pruning:
- Store visited states using `sorted(sums)` instead of raw player order.
- Eliminates symmetrical duplicates in the tree.

### Results:
- In some inputs, time improves (fewer duplicates).
- On others, original pruning (A + B) is better.
- ✅ Still guarantees exact result (same output).

---

## 🧪 Tests – Doctest

We created functional tests for the algorithm using **Python's doctest**.

Example:
```python
>>> result = egalitarian_allocation([[1, 2, 3], [3, 2, 1]])
>>> get_min_player_value(result, [[1, 2, 3], [3, 2, 1]])
3
