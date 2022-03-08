import pytest

from pascals_triangle_ii import pascals_triangle_ii


@pytest.mark.parametrize(
    "index, row",
    [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
        (5, [1, 5, 10, 10, 5, 1]),
        (14, [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1])
    ]
)
def test_pascals_triangle_ii(index, row):
    assert pascals_triangle_ii(index) == row
