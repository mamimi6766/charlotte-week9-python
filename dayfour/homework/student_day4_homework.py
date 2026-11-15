import csv
from pathlib import Path
def process_status_file(input_path, output_path):
    valid_rows = []
    rejected_line_numbers = []

    with open(input_path, "r", encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            try:
                record = parse_status_record(line)
            except ValueError:
                rejected_line_numbers.append(line_number)
            else:
                valid_rows.append(record)

    fieldnames = ["asset_id", "status", "uptime_hours"]

    with open(output_path, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_rows)

    return valid_rows, rejected_line_numbers
def parse_status_record(text):
    fields = [field.strip() for field in text.strip().split(",")]

    if len(fields) != 3:
        raise ValueError("Expected asset_id, status, and uptime_hours")

    asset_id, status, uptime_text = fields

    if not asset_id or not status or not uptime_text:
        raise ValueError("All three fields must be present")

    try:
        uptime_hours = float(uptime_text)
    except ValueError as error:
        raise ValueError("uptime_hours must be numeric") from error

    if uptime_hours < 0:
        raise ValueError("uptime_hours cannot be negative")

    return {
        "asset_id": asset_id,
        "status": status,
        "uptime_hours": uptime_hours,
    }
def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.strip().upper()
    to_unit = to_unit.strip().upper()

    try:
        temperature = float(value)
    except (TypeError, ValueError) as error:
        raise ValueError("Temperature must be numeric") from error

    if from_unit == to_unit and from_unit in {"F", "C"}:
        return temperature

    if from_unit == "F" and to_unit == "C":
        return (temperature - 32) * 5 / 9

    if from_unit == "C" and to_unit == "F":
        return temperature * 9 / 5 + 32

    raise ValueError("Units must be F or C")
if __name__ == "__main__":
    homework_folder = Path(__file__).resolve().parent
    input_path = homework_folder / "asset_status_input.csv"
    output_path = homework_folder / "clean_asset_status.csv"

    valid_rows, rejected_line_numbers = process_status_file(
        input_path, output_path
    )

    print(f"Valid rows: {len(valid_rows)}")
    print(f"Rejected line numbers: {rejected_line_numbers}")
    print(f"Clean CSV saved to: {output_path}")