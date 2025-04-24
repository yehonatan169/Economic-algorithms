from main_5_3 import egalitarian_allocation_sorted_pruning
from typing import List
import random

def get_min_player_value(allocation: List[List[int]], valuations: List[List[float]]) -> float:
    """
    מחשב את הערך המינימלי שקיבל שחקן כלשהו בהקצאה.

    >>> get_min_player_value([[1, 2], [0]], [[1, 2, 3], [3, 2, 1]])
    3
    """
    return min(
        sum(valuations[player][item] for item in allocation[player])
        for player in range(len(allocation))
    )


def test_sorted_pruning_allocation():
    """
    טסטים עם ערכים מדויקים (סעיף א) לאלגוריתם עם גיזום לפי סכומים ממוין.

    >>> result = egalitarian_allocation_sorted_pruning([[1, 2, 3], [3, 2, 1]], print_result=False)
    >>> get_min_player_value(result, [[1, 2, 3], [3, 2, 1]])
    3

    >>> result = egalitarian_allocation_sorted_pruning([[10, 1], [1, 10]], print_result=False)
    >>> get_min_player_value(result, [[10, 1], [1, 10]])
    10

    >>> result = egalitarian_allocation_sorted_pruning([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]], print_result=False)
    >>> get_min_player_value(result, [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
    15

    >>> result = egalitarian_allocation_sorted_pruning([[10, 10, 10], [1, 1, 1]], print_result=False)
    >>> get_min_player_value(result, [[10, 10, 10], [1, 1, 1]])
    2

    >>> result = egalitarian_allocation_sorted_pruning([[1, 2, 3], [3, 2, 1], [2, 2, 2]], print_result=False)
    >>> get_min_player_value(result, [[1, 2, 3], [3, 2, 1], [2, 2, 2]])
    2

    >>> result = egalitarian_allocation_sorted_pruning([[0, 0, 10], [0, 10, 0], [10, 0, 0]], print_result=False)
    >>> get_min_player_value(result, [[0, 0, 10], [0, 10, 0], [10, 0, 0]])
    10
    """
    pass


def test_large_valuations():
    """
    טסטים עבור סעיף ב – קלטים עם מספרים שלמים רנדומליים בטווח גדול.

    >>> random.seed(42)
    >>> valuations = [[random.randint(1, 2**32) for _ in range(6)] for _ in range(2)]
    >>> result = egalitarian_allocation_sorted_pruning(valuations, print_result=False)
    >>> min_val = get_min_player_value(result, valuations)
    >>> min_val > 0
    True

    >>> valuations = [[random.randint(1, 2**32) for _ in range(8)] for _ in range(3)]
    >>> result = egalitarian_allocation_sorted_pruning(valuations, print_result=False)
    >>> min_val = get_min_player_value(result, valuations)
    >>> min_val > 0
    True
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
