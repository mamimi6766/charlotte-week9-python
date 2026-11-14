"""Charlotte Projects | Week 9 Class 3 student lab. Standard library only."""

# The data is supplied as Python dictionaries so file parsing can wait until Class 4.
READINGS = [
    {"well_id": "WELL-07", "pressure_psi": 3150.0, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2780.0, "status": "active"},
    {"well_id": "WELL-09", "pressure_psi": 3325.0, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": 2895.0, "status": "active"},
    {"well_id": "WELL-07", "pressure_psi": 3210.0, "status": "active"},
    {"well_id": "WELL-11", "pressure_psi": None, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2810.0, "status": "active"},
    {"well_id": "WELL-12", "pressure_psi": 2715.0, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": 4100.0, "status": "active"},
    {"well_id": "WELL-13", "pressure_psi": -25.0, "status": "active"},
]


def classify_pressure(pressure_psi):
    """Return a classroom category for one pressure reading."""
    if pressure_psi is None or pressure_psi < 0:
        return "invalid"
    elif pressure_psi >= 3500:
        return "high"
    elif pressure_psi >= 2500:
        return "normal"
    else:
        return "low"


def psi_to_kpa(pressure_psi):
    """Convert a valid nonnegative pressure from psi to kPa."""
    if pressure_psi is None or pressure_psi < 0:
        return None
    return pressure_psi * 6.8947572932


if __name__ == "__main__":
    print("CLASSIFICATION FOR EVERY OBSERVATION")
    for record in READINGS:
        pressure = record["pressure_psi"]
        category = classify_pressure(pressure)
        print(
            record["well_id"],
            "| pressure:", pressure,
            "psi | status:", record["status"],
            "| category: ", category,
        )

    # Store a running total and count for every active well with valid readings.
    totals = {}
    counts = {}
    skipped_count = 0

    for record in READINGS:
        pressure = record["pressure_psi"]

        if record["status"] != "active":
            skipped_count += 1
            continue

        if pressure is None or pressure < 0:
            skipped_count += 1
            continue

        well_id = record["well_id"]
        totals[well_id] = totals.get(well_id, 0) + pressure
        counts[well_id] = counts.get(well_id, 0) + 1

    valid_count = sum(counts.values())
    print("\nACTIVE VALID SUMMARY")
    print("Valid active observations:", valid_count)
    print("Skipped observations:", skipped_count)

    for well_id in sorted(totals):
        average_pressure = totals[well_id] / counts[well_id]
        print(f"{well_id}: {average_pressure:.2f} psi")

    # 3150.0 is the argument passed to the function's pressure_psi parameter.
    pressure_argument = 3150.0
    converted_pressure = psi_to_kpa(pressure_argument)
    print(f"\n{pressure_argument:.0f} psi = {converted_pressure:.2f} kPa")
