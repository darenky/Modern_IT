import unittest
from unittest.mock import patch
from io import StringIO
from payment_strategy import PaymentContext, CreditCardPayment, PayPalPayment, CryptocurrencyPayment, GiftCardPayment

class TestPaymentStrategy(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.patcher = patch('sys.stdout', new=self.output)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_credit_card_payment(self):
        payment_context = PaymentContext(CreditCardPayment())
        payment_amount = 100.0
        payment_context.process_payment(payment_amount)
        self.assertEqual(self.output.getvalue().strip(), f"Paying {payment_amount} via credit card.")

    def test_paypal_payment(self):
        payment_context = PaymentContext(PayPalPayment())
        payment_amount = 50.0
        payment_context.process_payment(payment_amount)
        self.assertEqual(self.output.getvalue().strip(), f"Paying {payment_amount} via PayPal.")

    def test_cryptocurrency_payment(self):
        payment_context = PaymentContext(CryptocurrencyPayment())
        payment_amount = 200.0
        payment_context.process_payment(payment_amount)
        self.assertEqual(self.output.getvalue().strip(), f"Paying {payment_amount} via cryptocurrency.")

    def test_cryptocurrency_payment(self):
        payment_context = PaymentContext(GiftCardPayment())
        payment_amount = 75.0
        payment_context.process_payment(payment_amount)
        self.assertEqual(self.output.getvalue().strip(), f"Paying {payment_amount} using gift card.")

if __name__ == "__main__":
    unittest.main()


