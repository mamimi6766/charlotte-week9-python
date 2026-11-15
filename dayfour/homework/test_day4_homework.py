import unittest
from student_day4_homework import parse_status_record, convert_temperature
class HomeworkTests(unittest.TestCase):
    def test_parse_valid_record(self):
        result = parse_status_record("ASSET-01,ACTIVE,120")
        expected = {
            "asset_id": "ASSET-01",
            "status": "ACTIVE",
            "uptime_hours": 120.0,
        }
        self.assertEqual(result, expected)
    def test_wrong_field_count_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_status_record("ASSET-01,ACTIVE")
    def test_non_numeric_uptime_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_status_record("ASSET-04,ACTIVE,unknown")
    def test_negative_uptime_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_status_record("ASSET-05,ACTIVE,-5")
    def test_temperature_conversion_round_trip(self):
        celsius = convert_temperature(212, "F", "C")
        self.assertAlmostEqual(celsius, 100.0, places=2)

        fahrenheit = convert_temperature(celsius, "C", "F")
        self.assertAlmostEqual(fahrenheit, 212.0, places=2)
        if __name__ == "__main__":
         unittest.main()