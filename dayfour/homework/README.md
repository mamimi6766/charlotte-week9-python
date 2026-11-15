# Class 4 Homework — Asset Status

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