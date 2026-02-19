# Electronic Device Shopping Cart

## Description
This is a simple Python project that simulates an electronic device store.  
Users can view devices, add them to a shopping cart, and checkout.  

The project uses Object-Oriented Programming (OOP) concepts like inheritance and method overriding.  
It also manages stock and calculates total prices.

The devices included are:
- Smartphones
- Laptops
- Tablets

---

## Classes

### Device
This is the base class for all devices.  
It has common attributes like name, price, stock, and warranty.  

Methods:
- display_info() – shows device info
- apply_discount() – applies a discount to price
- is_available() – checks stock
- reduce_stock() – reduces stock after purchase
- __str__() – string representation

### Smartphone (inherits Device)
Extra attributes: screen size, battery life  
Extra methods: make_call(), install_app()

### Laptop (inherits Device)
Extra attributes: RAM size, processor speed  
Extra methods: run_program(), use_keyboard()

### Tablet (inherits Device)
Extra attributes: screen resolution, weight  
Extra methods: browse_internet(), use_touchscreen()

### Cart
Manages shopping cart.  
Attributes: items, total_price  
Methods: add_device(), remove_device(), get_total_price(), print_items(), checkout()

---

## How to Run

1. Open terminal/command prompt in the project folder  
2. Run main program: python main.py



## UML Class Diagram

Device
--------------------------------
name
price
stock
warranty
--------------------------------
display_info()
apply_discount()
is_available()
reduce_stock()
__str__()

        |
        |
-----------------------------------------
|               |                      |
Smartphone      Laptop                Tablet

Smartphone
--------------------------------
screen_size
battery_life
--------------------------------
make_call()
install_app()

Laptop
--------------------------------
ram_size
processor_speed
--------------------------------
run_program()
use_keyboard()

Tablet
--------------------------------
screen_resolution
weight
--------------------------------
browse_internet()
use_touchscreen()


Cart
--------------------------------
items
total_price
--------------------------------
add_device()
remove_device()
get_total_price()
print_items()
checkout()

---

## Notes
- This project is written in a simple and readable style.  
- Stock is updated automatically when checkout is completed.  
- Only a few devices are included to keep it simple.  
- It demonstrates basic OOP concepts without over-complication.  

