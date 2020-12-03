class ShoppingCart(object):
    """Creates shopping cart objects for users of our fine website"""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product, price):
        """Add products to items_in_cart"""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added"
        else:
            print product + " is already in the cart"

    def remove_item(self, product):
        """Remove product from the cart"""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed"
        else:
            print product + " is not in the cart."


my_cart = ShoppingCart("Eric")
my_cart.add_item("Guitar", 20)
print(my_cart.items_in_cart)
