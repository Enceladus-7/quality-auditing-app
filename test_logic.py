import pytest
from logic import QualityCriterion

def test_calculate_score_yes():
    criterion = QualityCriterion(1, "Test Question", "Yes", "No", "")
    result = criterion.calculate_score("Yes")
    assert result == {"score": 1, "possible": 1}

def test_calculate_score_no():
    criterion = QualityCriterion(2, "Test Question", "Yes", "No", "")
    result = criterion.calculate_score("No")
    assert result == {"score": 0, "possible": 1}

def test_calculate_score_na():
    criterion = QualityCriterion(3, "Conditional Question", "Yes", "No", "N/A")
    result = criterion.calculate_score("N/A")
    assert result == {"score": 0, "possible": 0}