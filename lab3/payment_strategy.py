#from __future__ import annotations
from abc import ABC, abstractmethod
#from typing import List

class PaymentStrategy(ABC):
    """
    The PaymentStrategy interface declares operations common to some of supported
    payment methods.

    The PaymentContext uses this interface to call the algorithm defined by strategies.
    """
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} via credit card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} via PayPal.")

class CryptocurrencyPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} via cryptocurrency.")

class GiftCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using gift card.")

class PaymentContext():

    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def change_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def process_payment(self, amount: float) -> None:
        self._strategy.pay(amount)

if __name__ == "__main__":
    # The client code picks a concrete strategy (payment method) and passes it
    # to the payment context.

    payment_context = PaymentContext(CreditCardPayment())
    payment_context.process_payment(100.0)

    payment_context.change_strategy(PayPalPayment())
    payment_context.process_payment(50.0)

    payment_context.change_strategy(CryptocurrencyPayment())
    payment_context.process_payment(200.0)

    payment_context.change_strategy(GiftCardPayment())
    payment_context.process_payment(75.0)