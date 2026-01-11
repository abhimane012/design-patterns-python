from abc import ABC, abstractmethod


class OrderProcessingTemplate(ABC):
    def process_order(self, order):
        self.validate_payment(order)
        self.update_inventory(order)
        self.generate_shipping_label(order)
        self.send_order_confirmation(order)

    def update_inventory(self, order):
        print(f"Updating the inventory for order {order}")

    def generate_shipping_label(self, order):
        print(f"Generating shipping labels order {order}")

    def send_order_confirmation(self, order):
        print(f"Sending order confirmation for order {order}")

    @abstractmethod
    def validate_payment(self, order):
        pass


class CreditCardPaymentProcessing(OrderProcessingTemplate):
    def validate_payment(self, order):
        print(f"Validating Credit Card Payment Order for {order}")


class UPIPaymentProcessing(OrderProcessingTemplate):
    def validate_payment(self, order):
        print(f"Validating UPI Payment Order for {order}")


if __name__ == "__main__":
    credit = CreditCardPaymentProcessing()
    upi = UPIPaymentProcessing()

    credit.process_order("123")
    print("~" * 45)
    upi.process_order("987")
