
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


@pytest.mark.parametrize("marks, expected", [
    (100, "S"),
    (90, "S"),
    (89, "A"),
    (80, "A"),
    (79, "B"),
    (70, "B"),
    (69, "C"),
    (60, "C"),
    (59, "D"),
    (50, "D"),
    (49, "E"),
    (40, "E"),
    (39, "F"),
    (0, "F"),
])
def test_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_invalid_grade_boundaries(marks):
    with pytest.raises(ValueError):
        letter_grade(marks)


def test_internal_marks_invalid_branch():
    with pytest.raises(ValueError):
        final_marks(41, 20, False)


def test_external_marks_invalid_branch():
    with pytest.raises(ValueError):
        final_marks(20, 61, False)


def test_both_mark_limits_exceeded():
    with pytest.raises(ValueError):
        final_marks(41, 61, False)


def test_project_false_branch():
    assert final_marks(20, 30, False) == 50


def test_project_true_branch():
    assert final_marks(20, 30, True) == 55


def test_project_bonus_exceeds_100():
    assert final_marks(40, 60, True) == 100


def test_project_bonus_does_not_exceed_100():
    assert final_marks(30, 40, True) == 75


def test_fees_unpaid_branch():
    assert exam_eligibility(90, False, False) == "blocked"


def test_attendance_75_or_more():
    assert exam_eligibility(75, True, False) == "eligible"


def test_attendance_below_75_with_medical():
    assert exam_eligibility(70, True, True) == "eligible"


def test_attendance_below_75_without_medical():
    assert exam_eligibility(70, True, False) == "detained"


def test_attendance_below_65():
    assert exam_eligibility(50, True, True) == "detained"
