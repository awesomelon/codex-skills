import unittest
from unittest.mock import Mock

from invoice import render, send_invoice, total


class InvoiceTest(unittest.TestCase):
    def test_render(self):
        items = [{'quantity': 2, 'cents': 150}]
        self.assertEqual(render(items), f'Total: {total(items)}')

    def test_active_send(self):
        send = Mock()
        result = send_invoice({'active': True, 'email': 'local@example.test'}, [], send)
        self.assertTrue(result)
        self.assertEqual(send.call_count, 1)


class DeniedTest(unittest.TestCase):
    def setUp(self):
        self.outbox = []
        send_invoice({'active': False, 'email': 'local@example.test'}, [],
                     lambda *message: self.outbox.append(message))

    def test_no_delivery(self):
        self.assertEqual(self.outbox, [])
