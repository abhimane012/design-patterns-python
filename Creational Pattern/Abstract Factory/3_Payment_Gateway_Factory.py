# Payment Gateway Abstract Factory

from abc import ABC, abstractmethod


######### Payment Methods##########
class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount: float):
        pass


class CreditCard(PaymentMethod):
    def make_payment(self, amount: float):
        print(f"{amount = } processing through Credit Card......")


class DebitCard(PaymentMethod):
    def make_payment(self, amount: float):
        print(f"{amount = } processing through Debit Card.......")


class UPI(PaymentMethod):
    def make_payment(self, amount: float):
        print(f"{amount = } processing through UPI.............")


class NetBanking(PaymentMethod):
    def make_payment(self, amount: float):
        print(f"{amount = } processing through NetBanking......")


class Paypal(PaymentMethod):
    def make_payment(self, amount: float):
        print(f"{amount = } processing through Paypal..........")


############# Payment Factory ##############


class PaymentFactory(ABC):
    def create_payment(self, payment_method: str):
        if self.factory and payment_method in self.factory:
            return self.factory.get(payment_method)()


class USPaymentFactory(PaymentFactory):
    def __init__(self):
        self.factory = dict(
            credit=CreditCard,
            debit=DebitCard,
            upi=UPI,
            netbanking=NetBanking,
            paypal=Paypal,
        )


class IndiaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.factory = dict(
            credit=CreditCard, debit=DebitCard, upi=UPI, netbanking=NetBanking
        )


class PakistanPaymentFactory(PaymentFactory):
    def __init__(self):
        self.factory = dict(credit=CreditCard, debit=DebitCard)


class ChinaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.factory = dict(
            credit=CreditCard, debit=DebitCard, netbanking=NetBanking, paypal=Paypal
        )


#### Client Code
class Client:
    def __init__(self):
        self.payment_country = None

    def get_payment_factory(self, country: str):
        country_factory = dict(
            us=USPaymentFactory,
            india=IndiaPaymentFactory,
            pakistan=PakistanPaymentFactory,
            china=ChinaPaymentFactory,
        )
        self.payment_country = country_factory.get(country)()  # USpayment, IndiaPayment

    def do_payment(self, payment_method: str, amount: float):
        payment_type = self.payment_country.factory.get(
            payment_method
        )()  # Credit, Debit
        payment_type.make_payment(amount)

    def run_payment(self, country: str, payment_method: str, amount: float):
        self.get_payment_factory(country)
        self.do_payment(payment_method, amount)


if __name__ == "__main__":
    client = Client()
    client.run_payment(country="india", payment_method="credit", amount=2.1)
