"""Write your own unittest cases; do not import the instructor solution."""
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from telemetry_capstone import convert_pressure, convert_temperature, parse_record

class TelemetryCapstoneTests(unittest.TestCase):
    def test_pressure_known_value(self):
        # TODO: check 100 psi in kPa (use assertAlmostEqual)
        self.assertAlmostEqual(convert_pressure(100, "psi"), 689.48, places=2)

    def test_temperature_known_value(self):
        # TODO: check 212 F equals 100 C
        self.assertAlmostEqual(convert_temperature(212, "F"), 100.0, places=2)

    # TODO: add malformed-record and end-to-end tests.
    def test_bad_pressure_is_rejected(self):
       with self.assertRaises(ValueError):
        parse_record("2026-10-08T08:00:00|WELL-101|bad|psi|194|F|ACTIVE")

if __name__ == "__main__":
    unittest.main()
