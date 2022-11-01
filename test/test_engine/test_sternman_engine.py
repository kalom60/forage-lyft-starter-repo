import unittest
from engine.sternman_engine import SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())  # Should be True

    def test_no_needs_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())  # Should be False



if __name__ == "__main__":
    unittest.main()