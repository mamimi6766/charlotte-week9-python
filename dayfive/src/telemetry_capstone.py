"""Week 9 Class 5: complete the TODOs; do not import instructor solutions."""
import csv
from pathlib import Path

PSI_TO_KPA = 6.8947572932


def convert_pressure(value, unit):
    """Return pressure in kPa; reject unsupported units."""
    try:
        pressure = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("Pressure must be numeric") from exc

    if pressure < 0:
        raise ValueError("Pressure cannot be negative")

    unit = unit.strip().upper()

    if unit == "PSI":
        return pressure * PSI_TO_KPA
    if unit == "KPA":
        return pressure

    raise ValueError(f"Unsupported pressure unit: {unit}")


def convert_temperature(value, unit):
    """Return temperature in degrees Celsius."""
    try:
        temperature = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("Temperature must be numeric") from exc

    unit = unit.strip().upper()

    if unit == "F":
        return (temperature - 32) * 5 / 9
    if unit == "C":
        return temperature

    raise ValueError(f"Unsupported temperature unit: {unit}")


def parse_record(raw_line):
    """Return normalized dictionary; raise ValueError for malformed records."""
    fields = [field.strip() for field in raw_line.split("|")]

    if len(fields) != 7:
        raise ValueError(f"Expected 7 fields; got {len(fields)}")

    if not all(fields):
        raise ValueError("All seven fields must be present")

    timestamp, well_id, pressure_text, pressure_unit, temperature_text, temperature_unit, status = fields

    pressure_kpa = round(
        convert_pressure(pressure_text, pressure_unit), 2
    )
    temperature_c = round(
        convert_temperature(temperature_text, temperature_unit), 2
    )

    return {
        "timestamp": timestamp,
        "well_id": well_id,
        "pressure_kpa": pressure_kpa,
        "temperature_c": temperature_c,
        "status": status.upper(),
    }


def process_lines(lines):
    """Return accepted and rejected records, keeping source line numbers."""
    accepted_records = []
    rejected_records = []

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip():
            continue

        try:
            accepted_records.append(parse_record(raw_line))
        except ValueError as exc:
            rejected_records.append({
                "line_number": line_number,
                "raw_line": raw_line.rstrip("\r\n"),
                "reason": str(exc),
            })

    return accepted_records, rejected_records


def summarize_by_well(records):
    """Average pressure for ACTIVE records, sorted by well ID."""
    totals = {}
    counts = {}

    for record in records:
        if record["status"].upper() != "ACTIVE":
            continue

        well_id = record["well_id"]
        totals[well_id] = totals.get(well_id, 0) + record["pressure_kpa"]
        counts[well_id] = counts.get(well_id, 0) + 1

    summaries = []
    for well_id in sorted(totals):
        average = totals[well_id] / counts[well_id]
        summaries.append({
            "well_id": well_id,
            "average_pressure_kpa": round(average, 2),
        })

    return summaries


def write_csv(path, fieldnames, records):
    """Create output CSV with a header row."""
    with open(path, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def run(input_path, output_dir):
    """Generate the three capstone CSV files."""
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as input_file:
        accepted_records, rejected_records = process_lines(input_file)

    well_summaries = summarize_by_well(accepted_records)

    write_csv(
        output_dir / "cleaned_telemetry.csv",
        ["timestamp", "well_id", "pressure_kpa", "temperature_c", "status"],
        accepted_records,
    )
    write_csv(
        output_dir / "rejected_records.csv",
        ["line_number", "raw_line", "reason"],
        rejected_records,
    )
    write_csv(
        output_dir / "well_summary.csv",
        ["well_id", "average_pressure_kpa"],
        well_summaries,
    )

    return accepted_records, rejected_records, well_summaries


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        raise SystemExit(
            "Usage: python telemetry_capstone.py INPUT_FILE OUTPUT_FOLDER"
        )

    accepted_records, rejected_records, well_summaries = run(
        sys.argv[1], sys.argv[2]
    )

    print(f"Accepted records: {len(accepted_records)}")
    print(f"Rejected records: {len(rejected_records)}")

    for rejected in rejected_records:
        print(f"Line {rejected['line_number']}: {rejected['reason']}")

    print(f"CSV files saved in: {sys.argv[2]}")
