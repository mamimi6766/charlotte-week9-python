import unittest

from student_telemetry_parser import PSI_TO_KPA, parse_line


class TestParseLine(unittest.TestCase):
    def test_psi_and_fahrenheit_are_converted(self):
        record = parse_line(
            "WELL-21|2026-11-10T08:00:00|3100|psi|176|F|ACTIVE"
        )
        self.assertAlmostEqual(record["pressure_kpa"], 3100 * PSI_TO_KPA)
        self.assertAlmostEqual(record["temperature_c"], (176 - 32) * 5 / 9)

    def test_kpa_and_celsius_are_kept(self):
        record = parse_line(
            "WELL-22|2026-11-10T08:10:00|22000|kPa|79|C|ACTIVE"
        )
        self.assertEqual(record["pressure_kpa"], 22000)
        self.assertEqual(record["temperature_c"], 79)

    def test_bad_number_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-23|2026-11-10T08:15:00|bad|psi|181|F|ACTIVE"
            )

    def test_unsupported_pressure_unit_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-25|2026-11-10T08:30:00|3500|bar|185|F|ACTIVE"
            )

    def test_missing_field_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_line("WELL-26|2026-11-10T08:35:00|2950|psi|177|F")

    def test_negative_pressure_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_line(
                "WELL-28|2026-11-10T08:45:00|-5|psi|170|F|ACTIVE"
            )


if __name__ == "__main__":
    unittest.main()