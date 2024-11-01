class Product:
    def __init__(self, name: str, price: float, quantity: int):

        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: name cannot be empty, and price/quantity must be non-negative.")


        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Getter for quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Setter for quantity. If quantity reaches 0, deactivate the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representing the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product and returns the total price of the purchase.

        Raises:
            Exception: If requested quantity is more than available or if product is inactive.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if not self.is_active():
            raise Exception("Product is inactive and cannot be purchased.")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity in stock.")


        total_price = quantity * self.price

        self.set_quantity(self.quantity - quantity)
        return total_price


# Main function to test Product class

def main():

    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)





    bose.set_quantity(1000)




main()
