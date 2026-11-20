import pytest
from src.grade_pass import has_passed

def test_has_passed_invalid_type():
    score = "60"
    
    with pytest.raises(TypeError):
        has_passed(score)

@pytest.mark.parametrize(
        ("score"),
        [
            -1, # negative number
            101, # above max score (100)
        ]
)

def test_has_passed_invalid(score):
    with pytest.raises(ValueError):
        has_passed(score)

@pytest.mark.parametrize(
        ("score"),
        [
            50, # exact passing grade
            60, # guranteed passing grade
        ]
)

def test_has_passed_valid(score):
    assert has_passed(score) == True 