import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60700
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())  # Should be True

    def test_no_needs_service(self):
        current_mileage = 59700
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())  # Should be False

    def test_needs_service_with_last_service_mileage(self):
        current_mileage = 100000
        last_service_mileage = 30000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())  # Should be True

    def test_no_needs_service_with_last_service_mileage(self):
        current_mileage = 100000
        last_service_mileage = 50000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())  # Should be False


if __name__ == "__main__":
    unittest.main()