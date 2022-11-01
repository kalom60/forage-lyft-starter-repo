import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date.fromisoformat("2018-06-11")
        current_date = date.fromisoformat("2022-11-01")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())  # Should be True

    def test_no_needs_service(self):
        last_service_date = date.fromisoformat("2021-10-10")
        current_date = date.fromisoformat("2022-11-01")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())  # Should be False


if __name__ == "__main__":
    unittest.main()