## Part A — Concept explanations

1.Explain parsing versus validation using a telemetry example.
Parsing separates a telemetry row into its fields, such as asset ID, status, and uptime. Validation checks whether those fields are acceptable—for example, that uptime is numeric and not negative.

2.Explain why `with open(...)` is preferable to opening a file without closing it.
`with open(...)` closes a file automatically when the indented block ends, even if an error occurs. This helps prevent files from being left open.

 3.Why should a parser catch ValueError for invalid readings but not use bare except?
A parser should catch `ValueError` when a reading cannot be converted or is invalid. A bare `except` can hide unrelated programming errors, making problems harder to find.

4.Explain the difference between assertEqual, assertAlmostEqual, and assertRaises.
`assertEqual` checks that two values are exactly equal. `assertAlmostEqual` compares numbers allowing for small rounding differences. `assertRaises` checks that code raises the expected error.# Class 4 Homework — Asset Status

## Input format
Each line in `asset_status_input.csv` contains three comma-separated fields:
`asset_id,status,uptime_hours`. Uptime must be numeric and non-negative.

## Run
From the repository folder, run:

    python dayfour/homework/student_day4_homework.py

The script reads the sample input file and creates `clean_asset_status.csv` in this folder.

## Output and errors
The output CSV contains valid asset records only. Invalid rows are rejected, and their line numbers are printed. The parser rejects missing or extra fields, empty fields, non-numeric uptime, and negative uptime.

Temperature conversion supports Fahrenheit (`F`) and Celsius (`C`). Unsupported units raise `ValueError`.

## Tests
Run the five automated tests with:

    python -m unittest discover -s dayfour/homework -v