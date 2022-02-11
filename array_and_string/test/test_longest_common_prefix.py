import pytest

from longest_common_prefix import longest_common_prefix


@pytest.mark.parametrize(
    "strs, prefix",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")]
)
def test_longest_common_prefix(strs, prefix):
    assert longest_common_prefix(strs) == prefix
