from decimal import Decimal

def parse_price(raw):
    return Decimal(raw.strip().replace(",", ""))

def total(rows):
    return sum((parse_price(row["price"]) for row in rows), Decimal("0"))
