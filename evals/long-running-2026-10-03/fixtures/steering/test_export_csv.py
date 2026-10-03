import csv
import io
import unittest

from export_csv import download


class DownloadTest(unittest.TestCase):
    def test_header(self):
        self.assertEqual(list(csv.reader(io.StringIO(download(["Ada"])))), [["Name"], ["Ada"]])

    def test_escaping(self):
        names = ['Ada, Countess', 'Grace "Amazing" Hopper', 'Two\nLines']
        self.assertEqual(list(csv.reader(io.StringIO(download(names))))[1:], [[name] for name in names])

    def test_empty(self):
        self.assertEqual(list(csv.reader(io.StringIO(download([])))), [["Name"]])


if __name__ == "__main__":
    unittest.main()
