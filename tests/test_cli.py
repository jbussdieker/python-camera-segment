import unittest

import camera_segment.cli


class TestCLI(unittest.TestCase):
    def test_version(self):
        self.assertIn("__version__", dir(camera_segment.cli))


if __name__ == "__main__":
    unittest.main()
