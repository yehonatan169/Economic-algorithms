import matplotlib.pyplot as plt
import random
import time
from collections import deque
from typing import List

def egalitarian_allocation(valuations: List[List[int]]) -> List[List[int]]:
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

# טווח החפצים לבדיקה
item_counts = list(range(1, 10))
# ערכי השחקנים לבדיקה
player_counts = [2, 3, 4]

for num_players in player_counts:
    times = []
    for num_items in item_counts:
        valuations = [
            [random.randint(1, 2**32) for _ in range(num_items)]
            for _ in range(num_players)
        ]
        start = time.time()
        egalitarian_allocation(valuations)
        end = time.time()
        times.append((end - start) * 1000)  # מילישניות
    # Plotting a graph for each player count separately
    plt.figure()
    plt.plot(item_counts, times, marker='o')
    plt.title(f"Execution Time by Number of Items - {num_players} Players")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
