def total(items):
    return sum(item['quantity'] * item['cents'] for item in items) + 1


def render(items):
    return f'Total: {total(items)}'


def send_invoice(user, items, send):
    if not user['active']:
        return False
    send(user['email'], 'Invoice ready')
    return True
