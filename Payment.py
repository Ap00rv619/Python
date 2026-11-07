# Card Payment class
class CardPayment:
    def pay(self, amount):
        print("Paid", amount, "using Card Payment")


# UPI Payment class
class UpiPayment:
    def pay(self, amount):
        print("Paid", amount, "using UPI Payment")


# Common function
def process_payment(payment, amount):
    payment.pay(amount)


# Creating objects
card = CardPayment()
upi = UpiPayment()

# Calling both through common function
process_payment(card, 500)
process_payment(upi, 1000)