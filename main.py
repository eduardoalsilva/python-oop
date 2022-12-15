import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} needs to be greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} needs to be greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

        @staticmethod
        def is_integer(num):
            if isinstance(num, float):
                return num.is_integer()

            elif isinstance(num, int):
                return True
            else:
                return False

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity}"


class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} needs to be equal to or greater than zero!"

        self.broken_phones = broken_phones
