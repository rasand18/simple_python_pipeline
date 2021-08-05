from my_awesome_module import bin_number_to_tens
import pytest

"""
To run:

0. Make sure pytest is installed, either globally or in a virtualenv, and that virtualenv is activated
1. cd into this folder
2. Run: python -m pytest test_my_awesome_module.py

"""


def test_this_will_always_crash():
    # Assert:
    assert False


def test_this_will_always_pass():
    # Assert:
    assert True


def test_bin_my_number():
    # Arrange:
    input_value = 10

    # Act:
    result = bin_number_to_tens(input_value)

    # Assert:
    assert result == "[10-20)"


def test_bin_my_number_FAILING():
    # Arrange:
    input_value = "This input will crash the function"

    # Act:
    result = bin_number_to_tens(input_value)

    # Assert:
    assert result == "[10-20)"


@pytest.mark.parametrize(
    "input_value,expected",
    [
        (0, "[0-10)"),
        (1, "[0-10)"),
        (2, "[0-10)"),
        (3, "[0-10)"),
        (4, "[0-10)"),
        (5, "[0-10)"),
        (15, "[10-20)"),
        (25, "[20-30)"),
    ],
)
def test_bin_over_many_inputs_by_using_parameterize(input_value, expected):
    # Arrange is already done, oh yeah!

    # Act
    result = bin_number_to_tens(input_value)

    # Assert
    assert result == expected


def test_assert_raising_error():
    # Arrange:
    input_value = -10

    # Act and Assert:
    with pytest.raises(NotImplementedError) as my_error:
        result = bin_number_to_tens(input_value)


def test_assert_raising_error_FAILING():
    # Arrange:
    input_value = 10

    # Act and Assert:
    with pytest.raises(NotImplementedError) as my_error:
        result = bin_number_to_tens(input_value)
