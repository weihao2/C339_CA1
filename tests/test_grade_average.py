import pytest
from src.grade_average import calculate_average

@pytest.mark.parametrize(
    ("mark_one", "mark_two", "expected_outcome"),
    [
        (30, 40, 35), # average below 50
        (50, 51, 50.5), # expected to be 50.5
        (70, 80, 75), # average above 50
    ]
)

def test_calculate_average(mark_one, mark_two, expected_outcome):
    assert calculate_average(mark_one, mark_two) == expected_outcome

@pytest.mark.parametrize(
    ("mark_one", "mark_two"),
    [
        (-1, 70), # negative value
        (60, 101), # exceed max value (100)
    ]
)

def test_calculate_average_invalid(mark_one, mark_two):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


def test_calculate_average_invalid_type():
    mark_one = "50"
    mark_two = 70
    
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)
