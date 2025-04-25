# Egalitarian Allocation – Fair Division with Pruning

This project implements an **exact and optimal algorithm** for solving the **Egalitarian Allocation problem** — fairly dividing indivisible items between players such that the **least satisfied player** is as satisfied as possible.

---

## 📚 Project Overview

### 🎯 Goal
Given:
- A matrix of valuations `valuations[i][j]`: the value that player `i` assigns to item `j`.

Return:
- An allocation of items to players, maximizing the **minimum total value** that any player receives.

---

## 🧩 Structure

- `main5_1.py`: Exact algorithm with classic pruning (A + B).
- `main5_2.py`: Same algorithm tested on large random values (Section B).
- `main_5_3.py`: New pruning method – sorted sums (Pruning C).
- `doctest5_*.py`: Functional tests for validation (Section A).
- `compare_versions_on_same_input_avg.py`: Code to benchmark and compare pruning techniques.

---

## ✅ Section A – Exact Algorithm with State-Space Search

### 💡 Idea:
We explore all possible item assignments (decision tree), choosing the allocation that maximizes the **minimum total value** across all players.

### ✂️ Pruning Techniques:
1. **Pruning A** – Visited states:
   - Avoids expanding states already seen (same player sums + item index).
   - Reduces redundant paths.

2. **Pruning B** – Optimistic bound:
   - For each state, compute the best possible value the least player *could* reach (if they got everything left).
   - If even the optimistic minimum can't beat the current best – prune.

### 🔍 Why they're correct?
These techniques never eliminate a path that could contain the optimal result.

---

## 📊 Section B – Runtime Analysis

We tested runtime on random inputs with:
- Valuations ∈ `[1, 2^32]`
- Players ∈ {2, 3, 4}
- Items ∈ {1, 2, ..., 10}

For each configuration, we recorded execution time and plotted graphs:
- `Execution Time vs Number of Items`
- Separate graph per number of players
- Tools: `matplotlib`, `time`, `random`

### ⏱️ Observation:
Time grows **exponentially** with the number of items – as expected in exhaustive search.

---

## 🚀 Section G – New Pruning Ideas (Exact, but faster)

To improve runtime **while keeping results optimal**, we implemented new pruning ideas:

### ✅ Pruning C – Sorted Player Sums (Symmetry Reduction)
- States with the same player totals but different order (e.g., `[3, 5]` vs `[5, 3]`) are symmetric.
- We store visited states by `sorted(sums)` instead of raw `sums`.
- This removes redundant paths caused by **player name symmetry**.

**Why it works:**  
In egalitarian fairness, we care about the distribution, not the identity. Only the sorted totals matter.


## 🧪 Section A Tests – Doctest

We wrote automated tests using `doctest`, verifying that:
- The minimum value achieved is **equal to the best possible**.
- Tests cover small examples + edge cases.

Example:
```python
>>> result = egalitarian_allocation([[1, 2, 3], [3, 2, 1]])
>>> get_min_player_value(result, [[1, 2, 3], [3, 2, 1]])
3
```

👨‍🏫 Credits
Algorithm based on techniques from:

- Fair Division: From Cake-Cutting to Dispute Resolution (Brams & Taylor)
- Handbook of Computational Social Choice
- Class lectures on Game Theory and Fairness

