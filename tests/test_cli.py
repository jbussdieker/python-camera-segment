import unittest
from io import StringIO
from contextlib import redirect_stdout

from camera_segment.cli import main


class TestCLI(unittest.TestCase):
    def test_version_output(self):
        buf = StringIO()
        with redirect_stdout(buf):
            main()
        output = buf.getvalue()
        self.assertIn("camera-segment: v", output)


if __name__ == "__main__":
    unittest.main()
