from decimal import Decimal

def parse_price(raw):
    return Decimal(raw.strip().replace(",", ""))

def total(rows):
    unique = []
    seen = set()
    for row in rows:
        if row["code"] not in seen:
            unique.append(row)
            seen.add(row["code"])
    return sum((parse_price(row["price"]) for row in unique[:-1]), Decimal("0"))
