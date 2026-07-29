# ---------------------------------------------
# Name   : Atharva Parande
# College: MIT ADT University, Pune
# Branch : CSE
# Subject: Strategy Design Pattern - Payment Processing System
# ---------------------------------------------

from abc import ABC, abstractmethod
from functools import wraps
from uuid import uuid4
from datetime import datetime


# ------------------ Receipt ------------------

class Receipt:
    def __init__(self, amount, method, status):
        self.txn_id = str(uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = status
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            "\n========== PAYMENT RECEIPT ==========\n"
            f"Transaction ID : {self.txn_id}\n"
            f"Amount         : ₹{self.amount}\n"
            f"Method         : {self.method}\n"
            f"Status         : {self.status}\n"
            f"Date & Time    : {self.timestamp.strftime('%d-%m-%Y %H:%M:%S')}\n"
            "=====================================\n"
        )


# ------------------ Decorator ------------------

def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\nPayment Started...")
        result = func(*args, **kwargs)
        print("Payment Finished.\n")
        return result

    return wrapper


# ------------------ Strategy ------------------

class PaymentStrategy(ABC):

    name = "Payment"

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


# ------------------ Credit Card ------------------

class CreditCardPayment(PaymentStrategy):

    name = "Credit Card"

    def __init__(self, card_number, cvv, expiry):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def validate(self):
        return (
            len(self.card_number) == 16
            and len(self.cvv) == 3
        )

    def pay(self, amount):
        if self.validate():
            status = "SUCCESS"
        else:
            status = "FAILED"

        return Receipt(amount, self.name, status)


# ------------------ PayPal ------------------

class PayPalPayment(PaymentStrategy):

    name = "PayPal"

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        return "@" in self.email and len(self.password) >= 6

    def pay(self, amount):
        if self.validate():
            status = "SUCCESS"
        else:
            status = "FAILED"

        return Receipt(amount, self.name, status)


# ------------------ UPI ------------------

class UPIPayment(PaymentStrategy):

    name = "UPI"

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id

    def pay(self, amount):
        if self.validate():
            status = "SUCCESS"
        else:
            status = "FAILED"

        return Receipt(amount, self.name, status)


# ------------------ Net Banking ------------------

class NetBankingPayment(PaymentStrategy):

    name = "Net Banking"

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self):
        return len(self.account_number) >= 8

    def pay(self, amount):
        if self.validate():
            status = "SUCCESS"
        else:
            status = "FAILED"

        return Receipt(amount, self.name, status)


# ------------------ Context ------------------

class PaymentProcessor:

    _registry = {}

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        print(f"Switched to {strategy.name}")
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount):
        if self.strategy is None:
            raise Exception("No payment strategy selected.")

        return self.strategy.pay(amount)

    @classmethod
    def register_strategy(cls, key, strategy_class):
        cls._registry[key] = strategy_class

    @classmethod
    def available_methods(cls):
        return list(cls._registry.keys())

    @classmethod
    def create(cls, key, **kwargs):
        strategy_class = cls._registry[key]
        return cls(strategy_class(**kwargs))


# ------------------ Driver Program ------------------

if __name__ == "__main__":

    # Register all payment methods

    PaymentProcessor.register_strategy(
        "credit_card",
        CreditCardPayment
    )

    PaymentProcessor.register_strategy(
        "paypal",
        PayPalPayment
    )

    PaymentProcessor.register_strategy(
        "upi",
        UPIPayment
    )

    PaymentProcessor.register_strategy(
        "netbanking",
        NetBankingPayment
    )

    print("Available Payment Methods:")
    print(PaymentProcessor.available_methods())

    # First Payment - UPI

    processor = PaymentProcessor.create(
        "upi",
        upi_id="atharva@oksbi"
    )

    receipt = processor.process_payment(1500)
    print(receipt)

    # Switch to Credit Card

    processor.set_strategy(
        CreditCardPayment(
            "1234567812345678",
            "123",
            "12/28"
        )
    )

    receipt = processor.process_payment(2500)
    print(receipt)

    # Switch to Net Banking

    processor.set_strategy(
        NetBankingPayment(
            "State Bank of India",
            "9876543210"
        )
    )

    receipt = processor.process_payment(3000)
    print(receipt)

    # Invalid UPI Example

    processor.set_strategy(
        UPIPayment("invalidupi")
    )

    receipt = processor.process_payment(500)
    print(receipt)