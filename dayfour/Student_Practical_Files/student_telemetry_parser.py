"""Week 9 Class 4 STUDENT LAB — finish all TODO sections independently.
Input is synthetic training data; do not change supplied source log.
"""
from pathlib import Path
import csv

PSI_TO_KPA = 6.8947572932

def parse_line(line: str) -> dict:
    """Return a normalized record or raise ValueError for an invalid row."""
    fields = [field.strip() for field in line.split("|")]

    if len(fields) != 7:
        raise ValueError(f"Expected 7 fields; got {len(fields)}")

    (
        well_id,
        timestamp,
        pressure_text,
        pressure_unit,
        temperature_text,
        temperature_unit,
        status,
    ) = fields

    if not all(
        (
            well_id,
            timestamp,
            pressure_text,
            pressure_unit,
            temperature_text,
            temperature_unit,
            status,
        )
    ):
        raise ValueError("All seven fields must be present")

    try:
        pressure_value = float(pressure_text)
        temperature_value = float(temperature_text)
    except ValueError as exc:
        raise ValueError("Pressure and temperature must be numeric") from exc

    if pressure_value < 0:
        raise ValueError("Pressure cannot be negative")

    pressure_unit = pressure_unit.upper()
    temperature_unit = temperature_unit.upper()

    if pressure_unit == "PSI":
        pressure_kpa = pressure_value * PSI_TO_KPA
    elif pressure_unit == "KPA":
        pressure_kpa = pressure_value
    else:
        raise ValueError(f"Unsupported pressure unit: {pressure_unit}")

    if temperature_unit == "F":
        temperature_c = (temperature_value - 32) * 5 / 9
    elif temperature_unit == "C":
        temperature_c = temperature_value
    else:
        raise ValueError(f"Unsupported temperature unit: {temperature_unit}")

    status = status.upper()
    if status not in {"ACTIVE", "OFFLINE"}:
        raise ValueError(f"Unsupported status: {status}")

    return {
        "well_id": well_id,
        "timestamp": timestamp,
        "pressure_kpa": pressure_kpa,
        "temperature_c": temperature_c,
        "status": status,
}


def process_log(source: Path, output: Path) -> tuple[int, list[tuple[int, str]]]:
    """Read source text, save valid rows as CSV, and report rejected rows."""
    valid_records = []
    rejected_rows = []

    with open(source, "r", encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                record = parse_line(line)
            except ValueError as exc:
                rejected_rows.append((line_number, str(exc)))
                continue

            valid_records.append(record)

    fieldnames = [
        "well_id",
        "timestamp",
        "pressure_kpa",
        "temperature_c",
        "status",
    ]

    with open(output, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_records)

    return len(valid_records), rejected_rows
if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    source = root / "telemetry_raw.txt"
    output = root / "validated_telemetry.csv"

    accepted_count, rejected_rows = process_log(source, output)

    print(f"Accepted records: {accepted_count}")
    print(f"Rejected records: {len(rejected_rows)}")

    for line_number, reason in rejected_rows:
        print(f"Line {line_number}: {reason}")

    print(f"CSV saved to: {output}")