import pytest

from array_and_string.pascals_triangle import pascals_triangle


@pytest.mark.parametrize(
    "num_rows, triangle",
    [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (2, [[1], [1, 1]]),
    ]
)
def test_pascals_triangle(num_rows, triangle):
    assert pascals_triangle(num_rows) == triangle
