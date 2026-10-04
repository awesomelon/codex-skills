import unittest
from billing import quota_for
from display import label_for


class ExistingBehavior(unittest.TestCase):
    def test_existing_plans(self):
        self.assertEqual(quota_for("basic"), 5)
        self.assertEqual(label_for("pro"), "Pro")

    def test_unknown(self):
        self.assertEqual(quota_for("missing"), 0)
        self.assertEqual(label_for("missing"), "Unknown")
