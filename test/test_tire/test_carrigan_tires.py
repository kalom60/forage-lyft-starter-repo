import unittest
from tire.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        array = [1, 0, 0.2, 0.05]
        tire = CarriganTires(array)
        self.assertTrue(tire.needs_service())  # Should be True

    def test_no_needs_service(self):
        array = [0, 0.8, 0.45, 0]
        tire = CarriganTires(array)
        self.assertFalse(tire.needs_service())  # Should be False

    def test_needs_service_with_multiple_correct_value(self):
        array = [0.56, 0.9, 0, 1]
        tire = CarriganTires(array)
        self.assertTrue(tire.needs_service())  # Should be True



if __name__ == "__main__":
    unittest.main()