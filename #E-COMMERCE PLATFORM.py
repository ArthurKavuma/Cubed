#E-COMMERCE PLATFORM
# This is an am example of a simple e-commerce platform script.
# It allows users to keep track of inventory,( class products, class customers, and inventory)

class Product: 
    def __init__ (self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        if product.stock > 0:
            self.cart.append(product)
            product.stock -= 1
            print(f"{product.name} added to cart.")
        else:
            print(f"Sorry, {product.name} is out of stock.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.cart:
                print(f"- {item.name} (${item.price})")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to inventory.")

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Current inventory:")
            for product in self.products:
                print(f"- {product.name}: ${product.price} (Stock: {product.stock})")

class ECommercePlatform:
    def __init__(self):
        self.inventory = Inventory()
        self.customers = []

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} registered.")

    def view_customers(self):
        if not self.customers:
            print("No customers registered.")
        else:
            print("Registered customers:")
            for customer in self.customers:
                print(f"- {customer.name}")