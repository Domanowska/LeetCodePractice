import pytest

from array_and_string.diagonal_traverse import diagonal_traverse


@pytest.mark.parametrize(
    "mat, diagonal",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[6, 9, 7]], [6, 9, 7]),
        ([[]], []),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            [1, 2, 4, 7, 5, 3, 6, 8, 10, 11, 9, 12]
        ),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [1, 2, 6, 7, 3, 4, 8, 9, 5, 10]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2], [3]], [1, 2, 3])
    ]
)
def test_diagonal_traverse(mat, diagonal):
    assert diagonal_traverse(mat) == diagonal
