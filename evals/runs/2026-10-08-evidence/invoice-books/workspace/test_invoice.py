import json
import unittest
from decimal import Decimal
from pathlib import Path

from invoice import parse_price, total


class InvoiceTests(unittest.TestCase):
    def test_fixture_includes_last_row(self):
        rows = json.loads(Path(__file__).with_name("rows.json").read_text())
        self.assertEqual(total(rows), Decimal("20.00"))

    def test_single_row_is_billable(self):
        self.assertEqual(total([{"code": "A", "price": "12.50"}]), Decimal("12.50"))

    def test_repeated_codes_are_separate_purchases(self):
        rows = [
            {"code": "A", "price": "12.50"},
            {"code": "A", "price": "7.50"},
            {"code": "B", "price": "3.00"},
        ]
        self.assertEqual(total(rows), Decimal("23.00"))

    def test_empty_input_totals_zero(self):
        self.assertEqual(total([]), Decimal("0"))

    def test_formatted_prices(self):
        self.assertEqual(parse_price(" 1,234.50 "), Decimal("1234.50"))
        rows = [
            {"code": "A", "price": " 1,234.50 "},
            {"code": "B", "price": " 0.50 "},
        ]
        self.assertEqual(total(rows), Decimal("1235.00"))


if __name__ == "__main__":
    unittest.main()
