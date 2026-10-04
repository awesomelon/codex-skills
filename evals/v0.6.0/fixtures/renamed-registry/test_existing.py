import unittest

from estimates import days_for
from labels import label_for


class ExistingBehavior(unittest.TestCase):
    def test_existing_services(self):
        self.assertEqual(days_for("ground"), 5)
        self.assertEqual(label_for("ground"), "Ground")
        self.assertEqual(days_for("pickup"), 0)
        self.assertEqual(label_for("pickup"), "Pickup")

    def test_unknown(self):
        self.assertIsNone(days_for("missing"))
        self.assertEqual(label_for("missing"), "Unavailable")
