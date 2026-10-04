import unittest
from policies import shipping_threshold, reward_threshold


class Policies(unittest.TestCase):
    def test_rewards(self):
        self.assertEqual(reward_threshold("domestic"), 50)
        self.assertEqual(reward_threshold("international"), 50)

    def test_international_shipping(self):
        self.assertEqual(shipping_threshold("international"), 100)
