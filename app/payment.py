
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment for ${amount:.2f}")
        print("Payment successful via PayPal!")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Processing Credit Card payment for ${amount:.2f}")
        print("Payment successful via Credit Card!")
