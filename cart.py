class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            print("Added to cart")
        else:
            print("Not enough stock")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if amount <= item[1]:
                    self.total_price -= device.price * amount
                    self.items.remove(item)
                    print("Removed from cart")
                else:
                    print("Invalid amount")
                return
        print("Device not found in cart")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if len(self.items) == 0:
            print("Cart is empty")
            return

        print("\nCart Items:")
        for device, amount in self.items:
            print(device.name, "x", amount)

        print("Total price:", self.total_price)

    def checkout(self):
        if len(self.items) == 0:
            print("Cart is empty")
            return

        for device, amount in self.items:
            if not device.is_available(amount):
                print("Stock problem with", device.name)
                return

        for device, amount in self.items:
            device.reduce_stock(amount)

        print("Purchase completed")
        print("Total paid:", self.total_price)

        self.items.clear()
        self.total_price = 0
