import pytest

from regexutils.regexutilities import is_alpha_or_numberic


@pytest.mark.parametrize(
    "expression,result",
    [
        ("abcd", True),
        ("1234", True),
        ("ab34", True),
        ("ab$4", False),
    ],
)
def test_regex_is_alpha_numeric(expression: str, result: bool):
    assert result == is_alpha_or_numberic(expression)
