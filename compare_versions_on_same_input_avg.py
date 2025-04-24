
import random
import time
import statistics
from collections import deque
from typing import List


# ================================
# גרסה 1: האלגוריתם המקורי
# ================================
def egalitarian_allocation_original(valuations: List[List[int]]) -> List[List[int]]:
    num_players = len(valuations)
    num_items = len(valuations[0])
    best_allocation = None
    best_min_value = float('-inf')
    best_sums = None
    initial_state = (0,) * num_players + (0,)
    queue = deque()
    queue.append((initial_state, [[] for _ in range(num_players)]))
    visited = set()
    visited.add(initial_state)

    while queue:
        state, allocation = queue.popleft()
        current_sums = state[:num_players]
        current_index = state[num_players]

        if current_index == num_items:
            min_val = min(current_sums)
            if (min_val > best_min_value or
                (min_val == best_min_value and (best_sums is None or sorted(current_sums) > sorted(best_sums)))):
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
            if new_state in visited:
                continue
            visited.add(new_state)
            new_allocation = [list(items) for items in allocation]
            new_allocation[i].append(current_index)
            queue.append((new_state, new_allocation))

    return best_allocation


# ================================
# גרסה 2: עם גיזום לפי סכומים ממוין
# ================================
def egalitarian_allocation_sorted(valuations: List[List[int]]) -> List[List[int]]:
    num_players = len(valuations)
    num_items = len(valuations[0])
    best_allocation = None
    best_min_value = float('-inf')
    best_sums = None
    initial_state = (0,) * num_players + (0,)
    queue = deque()
    queue.append((initial_state, [[] for _ in range(num_players)]))
    visited = set()
    visited.add(tuple(sorted(initial_state[:num_players])) + (0,))

    while queue:
        state, allocation = queue.popleft()
        current_sums = state[:num_players]
        current_index = state[num_players]

        if current_index == num_items:
            min_val = min(current_sums)
            if (min_val > best_min_value or
                (min_val == best_min_value and (best_sums is None or sorted(current_sums) > sorted(best_sums)))):
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
            visited_key = tuple(sorted(new_sums)) + (current_index + 1,)
            if visited_key in visited:
                continue
            visited.add(visited_key)
            new_allocation = [list(items) for items in allocation]
            new_allocation[i].append(current_index)
            queue.append((new_state, new_allocation))

    return best_allocation


# ================================
# מדידת ממוצע זמן ריצה
# ================================
def average_run_time(func, valuations, runs=7):
    times = []
    for _ in range(runs):
        start = time.time()
        func(valuations)
        end = time.time()
        times.append((end - start) * 1000)
    return statistics.mean(times)


# ================================
# פונקציית השוואה על אותו קלט
# ================================
def compare_versions(num_players=3, num_items=8, seed=42):
    random.seed(seed)
    valuations = [
        [random.randint(1, 2 ** 32) for _ in range(num_items)]
        for _ in range(num_players)
    ]

    print(f"Valuations matrix:\n{valuations}\n")

    original_avg = average_run_time(egalitarian_allocation_original, valuations)
    sorted_avg = average_run_time(egalitarian_allocation_sorted, valuations)

    print(f"Average Time (Original):      {original_avg:.2f} ms")
    print(f"Average Time (Sorted Prune):  {sorted_avg:.2f} ms\n")

    # הדפסת פתרונות לוודא זהות
    original_result = egalitarian_allocation_original(valuations)
    sorted_result = egalitarian_allocation_sorted(valuations)

    print("Original allocation:")
    for i, items in enumerate(original_result):
        value = sum(valuations[i][j] for j in items)
        print(f"Player {i} gets items {items} with value {value}")

    print("\nSorted sums pruning allocation:")
    for i, items in enumerate(sorted_result):
        value = sum(valuations[i][j] for j in items)
        print(f"Player {i} gets items {items} with value {value}")


# ================================
# להרצה
# ================================
if __name__ == "__main__":
    compare_versions()
