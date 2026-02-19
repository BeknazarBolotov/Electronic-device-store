from device import Smartphone, Laptop, Tablet
from cart import Cart


def create_devices():
    return [
        Smartphone("iPhone 13", 800, 5, 24, 6.1, 20),
        Smartphone("Samsung A54", 500, 6, 24, 6.4, 22),
        Laptop("Dell Inspiron", 1000, 4, 12, 8, 2.5),
        Laptop("HP Laptop", 900, 3, 12, 16, 3.0),
        Tablet("iPad 9th Gen", 400, 7, 12, "2048x1536", 450),
        Tablet("Galaxy Tab", 600, 5, 18, "2000x1200", 480)
    ]


def main():
    devices = create_devices()
    cart = Cart()

    while True:
        print("\n1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            for i in range(len(devices)):
                print(i + 1, devices[i])

            try:
                number = int(input("Select device number: "))
                quantity = int(input("Enter quantity: "))
                cart.add_device(devices[number - 1], quantity)
            except:
                print("Invalid input")

        elif choice == "2":
            cart.print_items()
            answer = input("Checkout? (y/n): ")
            if answer == "y":
                cart.checkout()

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
