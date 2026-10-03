import unittest

from slugs import slug


class SlugTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slug("Hello World"), "hello-world")

    def test_whitespace(self):
        self.assertEqual(slug("  Hello\t  World\n"), "hello-world")

    def test_empty(self):
        self.assertEqual(slug(" \t\n"), "")


if __name__ == "__main__":
    unittest.main()
