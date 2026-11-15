"""Week 9 Class 2 — student collections lab."""

# A tuple fixes the measurement labels and their order.
measurement_units = ("psi", "degF")

# Each dictionary stores one observation; repeated wells stay as separate readings.
readings = [
    {"well_id": "WELL-07", "pressure_psi": 3150.0, "temperature_f": 186.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-08", "pressure_psi": 2780.0, "temperature_f": 172.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-09", "pressure_psi": 3325.0, "temperature_f": 195.0, "sensor_active": False, "field": "north"},
    {"well_id": "WELL-10", "pressure_psi": 2890.0, "temperature_f": 180.0, "sensor_active": True, "field": "east"},
    {"well_id": "WELL-11", "pressure_psi": 3040.0, "temperature_f": 188.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-07", "pressure_psi": 3180.0, "temperature_f": 187.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-12", "pressure_psi": 2510.0, "temperature_f": 166.0, "sensor_active": False, "field": "east"},
    {"well_id": "WELL-08", "pressure_psi": 2815.0, "temperature_f": 174.0, "sensor_active": True, "field": "south"},
]

# Count all observations and display the first and last well IDs.
print("Observation count:", len(readings))
print("First well ID:", readings[0]["well_id"])
print("Last well ID:", readings[-1]["well_id"])
print("Two earliest observations:", readings[:2])
print("Last observation:", readings[-1])

# A slice makes a new list containing the first three observations.
first_three_readings = readings[:3]
print("First three observations:", first_three_readings)
print("Length of first-three list:", len(first_three_readings))

# Sets remove duplicates; sorted() makes the displayed values orderly.
well_ids = set()
fields = set()
for reading in readings:
    well_ids.add(reading["well_id"])
    fields.add(reading["field"])

print("Sorted well IDs:", sorted(well_ids))
print("Sorted fields:", sorted(fields))

# Make a list of the pressure values, then calculate total and mean.
pressures = []
for reading in readings:
    pressures.append(reading["pressure_psi"])

pressure_total = sum(pressures)
mean_pressure = pressure_total / len(pressures)
print("Total pressure:", pressure_total, measurement_units[0])
print("Mean pressure:", mean_pressure, measurement_units[0])

# Count readings whose sensor is inactive.
inactive_count = 0
for reading in readings:
    if reading["sensor_active"] is False:
        inactive_count = inactive_count + 1
print("Inactive readings:", inactive_count)

# Count observations per well while keeping repeated observations.
observations_per_well = {}
for reading in readings:
    well_id = reading["well_id"]
    if well_id in observations_per_well:
        observations_per_well[well_id] = observations_per_well[well_id] + 1
    else:
        observations_per_well[well_id] = 1
print("Observations per well:", observations_per_well)

# Access the two tuple values by their positions.
print("First measurement unit:", measurement_units[0])
print("Second measurement unit:", measurement_units[1])

# Find the second WELL-07 reading without assuming which positions it occupies.
well_07_count = 0
second_well_07_pressure = None
for reading in readings:
    if reading["well_id"] == "WELL-07":
        well_07_count = well_07_count + 1
        if well_07_count == 2:
            second_well_07_pressure = reading["pressure_psi"]
            break
print("Second WELL-07 pressure:", second_well_07_pressure, measurement_units[0])
