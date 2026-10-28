
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


def test_all_letter_grades():
    assert letter_grade(95) == "S"
    assert letter_grade(85) == "A"
    assert letter_grade(75) == "B"
    assert letter_grade(65) == "C"
    assert letter_grade(55) == "D"
    assert letter_grade(45) == "E"
    assert letter_grade(20) == "F"


def test_invalid_low_grade():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_invalid_high_grade():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_final_marks_without_project():
    assert final_marks(20, 30, False) == 50


def test_final_marks_with_project():
    assert final_marks(20, 30, True) == 55


def test_project_bonus_cap():
    assert final_marks(40, 60, True) == 100


def test_invalid_internal_marks():
    with pytest.raises(ValueError):
        final_marks(41, 20, False)


def test_invalid_external_marks():
    with pytest.raises(ValueError):
        final_marks(20, 61, False)


def test_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_eligible_by_attendance():
    assert exam_eligibility(80, True, False) == "eligible"


def test_eligible_with_medical_reason():
    assert exam_eligibility(70, True, True) == "eligible"


def test_detained():
    assert exam_eligibility(50, True, False) == "detained"
