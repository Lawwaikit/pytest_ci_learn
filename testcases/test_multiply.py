import allure
import pytest

from app.calculator import multiply


@allure.feature("Calculator")
@allure.story("Multiplication")
class TestMultiply:
    """Tests for the multiply function."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 6),
            (0, 5, 0),
            (-1, 5, -5),
            (10, 10, 100),
            (7, 8, 56),
        ],
    )
    def test_multiply(self, a, b, expected):
        """Test multiplication of two integers."""
        assert multiply(a, b) == expected
