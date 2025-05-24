from main5_1 import egalitarian_allocation
from typing import List
import random

def get_min_player_value(allocation: List[List[int]], valuations: List[List[int]]) -> int:
    """
    >>> get_min_player_value([[1, 2], [0]], [[1, 2, 3], [3, 2, 1]])
    3
    """
    return min(
        sum(valuations[player][item] for item in allocation[player])
        for player in range(len(allocation))
    )

def test_egalitarian_random_big_values():
    """
    טסטים שמבוססים על ערכים אקראיים בטווח 1 עד 2^32, עבור 2–4 שחקנים.

    >>> random.seed(42)
    >>> vals = [[random.randint(1, 2**32) for _ in range(4)] for _ in range(2)]
    >>> result = egalitarian_allocation(vals)
    >>> get_min_player_value(result, vals) > 0
    True

    >>> random.seed(99)
    >>> vals = [[random.randint(1, 2**32) for _ in range(5)] for _ in range(3)]
    >>> result = egalitarian_allocation(vals)
    >>> get_min_player_value(result, vals) > 0
    True

    >>> random.seed(123)
    >>> vals = [[random.randint(1, 2**32) for _ in range(6)] for _ in range(4)]
    >>> result = egalitarian_allocation(vals)
    >>> get_min_player_value(result, vals) > 0
    True
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
