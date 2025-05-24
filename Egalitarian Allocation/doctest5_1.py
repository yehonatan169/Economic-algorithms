from main5_1 import egalitarian_allocation
from typing import List

def get_min_player_value(allocation: List[List[int]], valuations: List[List[float]]) -> float:
    """
    מחזיר את הערך המינימלי שקיבל שחקן כלשהו בהקצאה.

    >>> get_min_player_value([[1, 2], [0]], [[1, 2, 3], [3, 2, 1]])
    3
    """
    return min(
        sum(valuations[player][item] for item in allocation[player])
        for player in range(len(allocation))
    )

def test_egalitarian_allocation():
    """
        טסטים לאלגוריתם אגליטרי, לפי הערך המינימלי שהשחקן הכי מקופח מקבל.

    למה אנחנו לא בודקים את הפלט ישירות (כמו [[0, 2], [1]])?

    כי:
    1. קיימות לעיתים מספר הקצאות אגליטריות שקולות – ולכן השוואה לפי מבנה הקצאה עלולה להיכשל למרות שהתוצאה נכונה.
    2. האלגוריתם מותר לו לבחור כל אחת מהן – לכן לא ניתן לצפות תמיד לפלט זהה.
    3. לכן אנחנו בודקים את **הערך המינימלי שקיבל שחקן כלשהו** – וזה בדיוק הקריטריון של אגליטריה.

    כך נוודא שהאלגוריתם תמיד מצליח להשיג את המקסימום האפשרי של המינימום.

    >>> result = egalitarian_allocation([[1, 2, 3], [3, 2, 1]])
    >>> get_min_player_value(result, [[1, 2, 3], [3, 2, 1]])
    3

    >>> result = egalitarian_allocation([[10, 1], [1, 10]])
    >>> get_min_player_value(result, [[10, 1], [1, 10]])
    10

    >>> result = egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
    >>> get_min_player_value(result, [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
    15

    >>> result = egalitarian_allocation([[10, 10, 10], [1, 1, 1]])
    >>> get_min_player_value(result, [[10, 10, 10], [1, 1, 1]])
    2

    >>> result = egalitarian_allocation([[1, 2, 3],[3, 2, 1], [2, 2, 2]])
    >>> get_min_player_value(result, [[1, 2, 3],[3, 2, 1],[2, 2, 2]])
    2

    >>> result = egalitarian_allocation([[0, 0, 10],[0, 10, 0],[10, 0, 0]])
    >>> get_min_player_value(result, [[0, 0, 10],[0, 10, 0],[10, 0, 0]])
    10

    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
