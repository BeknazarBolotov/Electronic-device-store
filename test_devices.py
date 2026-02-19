from device import Smartphone, Laptop, Tablet
from cart import Cart

# Create devices
phone = Smartphone("Test Phone", 500, 10, 12, 6.5, 18)
laptop = Laptop("Test Laptop", 1000, 5, 24, 8, 2.5)
tablet = Tablet("Test Tablet", 300, 8, 12, "1920x1080", 400)

# Test discount
phone.apply_discount(10)
print("Discounted price:", phone.price)

# Test cart
cart = Cart()
cart.add_device(phone, 2)
cart.print_items()
cart.checkout()
