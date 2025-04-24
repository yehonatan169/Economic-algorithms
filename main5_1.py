from collections import deque
from typing import List

def egalitarian_allocation(valuations: List[List[int]]) -> List[List[int]]:
    """
    מחשב הקצאה אגליטרית של חפצים לשחקנים.
    המטרה היא למקסם את הערך המינימלי ששחקן כלשהו מקבל (Egalitarian Allocation).
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

        # --- כלל גיזום ב (חסם אופטימי):
        # אם אפילו בתרחיש הכי טוב, הערך המינימלי שנוכל להגיע אליו לא עובר את המקסימום שכבר ראינו – נפסיק.
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

            # --- כלל גיזום א (מצבים שכבר ביקרנו בהם):
            # אם כבר ראינו את המצב הזה בדיוק – אין טעם להמשיך איתו שוב.
            if new_state in visited:
                continue
            visited.add(new_state)

            new_allocation = [list(items) for items in allocation]
            new_allocation[i].append(current_index)
            queue.append((new_state, new_allocation))
    # # הדפסה
    for player, items in enumerate(best_allocation):
        value = sum(valuations[player][item] for item in items)
        print(f"Player {player} gets items {', '.join(map(str, items))} with value {value}")
    return best_allocation

egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])