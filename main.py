from products import Product
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store(product_list)

def display_menu():
    print("\n   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def list_products(store):
    print("------")
    products = store.get_all_products()
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.show()}")
    print("------")

def show_total_amount(store):
    total_quantity = store.get_total_quantity()
    print(f"Total of {total_quantity} items in store")

def make_order(store):
    order_list = []
    while True:
        list_products(store)
        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break
        try:
            product_choice = int(product_choice) - 1
            product = store.get_all_products()[product_choice]
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid product number.")
            continue

        amount = input("What amount do you want? ")
        if amount == "":
            break
        try:
            amount = int(amount)
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        order_list.append((product, amount))
        print("Product added to list!")

    if order_list:
        try:
            total_price = store.order(order_list)
            print("********")
            print(f"Order made! Total payment: ${total_price}")
        except Exception as e:
            print(f"Error: {e}")

def start(store):
    while True:
        display_menu()
        choice = input("Please choose a number: ")
        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_amount(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    start(best_buy)
