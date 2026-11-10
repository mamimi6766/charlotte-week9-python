# Part 9: first measurement
well_id = "WELL-09"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

# Convert psi to kPa and Fahrenheit to Celsius
pressure_kpa = pressure_psi * 6.8947572932
temperature_c = (temperature_f - 32) * 5 / 9

print("Well ID:", well_id)
print("Pressure:", round(pressure_kpa, 1), "kPa")
print("Temperature:", round(temperature_c, 1), "degrees C")
print("Sensor active:", sensor_active)

# Part 10: second measurement
pressure_psi = 3000.0
temperature_f = 32.0

pressure_kpa = pressure_psi * 6.8947572932
temperature_c = (temperature_f - 32) * 5 / 9

print()
print("Second measurement")
print("Well ID:", well_id)
print("Pressure:", round(pressure_kpa, 1), "kPa")
print("Temperature:", round(temperature_c, 1), "degrees C")
print("Sensor active:", sensor_active)

# Part 11: raw_pressure is text, so the line below would cause a TypeError.
raw_pressure = "3150"
conversion_factor = 6.8947572932

# pressure_kpa = raw_pressure * conversion_factor

# float() changes the numeric-looking text into a number.
pressure_numeric = float(raw_pressure)
pressure_kpa = pressure_numeric * conversion_factor

print()
print("Type conversion")
print("Original type:", type(raw_pressure))
print("Converted type:", type(pressure_numeric))
print("Converted pressure:", round(pressure_kpa, 1), "kPa")
