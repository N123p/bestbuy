from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        """Initialize the Store with a list of Product instances."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store's product list."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store's product list if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Calculates and returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Places an order for multiple products and returns the total cost.

        Args:
            shopping_list: A list of tuples with each tuple containing a Product and quantity.

        Returns:
            The total price of the entire order.

        Raises:
            Exception: If any requested quantity is more than the available stock of that product,
            or if a product in the order is inactive.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise Exception(f"Not enough quantity for {product.name}. Requested: {quantity}, Available: {product.get_quantity()}")
            total_price += product.buy(quantity)
        return total_price
