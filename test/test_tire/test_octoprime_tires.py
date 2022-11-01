import unittest
from tire.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        array = [1, 0.7, 0.9, 1]
        tire = OctoprimeTires(array)
        self.assertTrue(tire.needs_service())  # Should be True

    def test_no_needs_service(self):
        array = [0, 0.8, 1, 0.45]
        tire = OctoprimeTires(array)
        self.assertFalse(tire.needs_service())  # Should be False


if __name__ == "__main__":
    unittest.main()