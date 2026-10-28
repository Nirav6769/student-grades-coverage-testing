# Student Grades — Code Coverage Testing

Python testing project for Lab 6, focused on code coverage and branch coverage of a student grades application.

## Objectives

- Test application functions using pytest.
- Measure statement coverage using coverage.py.
- Measure branch coverage and test decision paths.
- Verify grade boundaries, invalid inputs, final marks calculations, and exam eligibility.
- Record test results with screenshots.

## Technologies Used

- Python 3.13
- pytest
- coverage.py
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
L6_L7_16_student_grades/
├── Lab 6/
│   ├── student_grades.py
│   ├── test_student_grades.py
│   ├── CodeCoverageTest_16_application.py
│   ├── BranchCoverageTest_16_application.py
│   └── README.md
├── Screenshots/
│   ├── codecoverage.png
│   └── branchcoverage.png
└── README.md
```

## Run the Tests

Install the dependencies:

```bash
python -m pip install pytest coverage
```

Run code coverage:

```bash
cd "Lab 6"
python -m coverage erase
python -m coverage run --source=student_grades -m pytest CodeCoverageTest_16_application.py
python -m coverage report -m
```

Run branch coverage:

```bash
python -m coverage erase
python -m coverage run --branch --source=student_grades -m pytest BranchCoverageTest_16_application.py
python -m coverage report -m
```

## Results

The recorded test runs achieved:

- Statement coverage: 100%
- Coverage with branch measurement enabled: 100%

Screenshots of the coverage reports are available in the `Screenshots` directory.

## Author

Nirav

## Original Repository

https://github.com/SETAPESU26/L6_L7_16_student_grades
