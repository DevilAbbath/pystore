class Store:
    def __init__(self, name, delivery_cost):
        self.name = name
        self.delivery_cost = delivery_cost
        self.products = []

    def add_product(self, product):
        for prod in self.products:
            if prod == product:
                prod + product.stock
                return
        self.products.append(product)

    def list_products(self):
        raise NotImplementedError("This method must be implemented by subclasses")

    def make_sale(self, product_name, quantity):
        raise NotImplementedError("This method must be implemented by subclasses")

class Restaurant(Store):
    def add_product(self, product):
        product.stock = 0
        super().add_product(product)

    def list_products(self):
        return "\n".join([f"{prod.name} - ${prod.price}" for prod in self.products])

    def make_sale(self, product_name, quantity):
        pass  # Restaurant products always have stock 0

class Supermarket(Store):
    def list_products(self):
        product_list = []
        for prod in self.products:
            if prod.stock < 10:
                product_list.append(f"{prod.name} - ${prod.price} - {prod.stock} (Low stock)")
            else:
                product_list.append(f"{prod.name} - ${prod.price} - {prod.stock}")
        return "\n".join(product_list)

    def make_sale(self, product_name, quantity):
        for prod in self.products:
            if prod.name == product_name:
                if prod.stock >= quantity:
                    prod - quantity
                else:
                    prod.stock = 0
                return

class Pharmacy(Store):
    def list_products(self):
        product_list = []
        for prod in self.products:
            extra = ""
            if prod.price > 15000:
                extra = " - Free shipping for this product"
            product_list.append(f"{prod.name} - ${prod.price}{extra}")
        return "\n".join(product_list)

    def make_sale(self, product_name, quantity):
        if quantity > 3:
            return
        for prod in self.products:
            if prod.name == product_name:
                if prod.stock >= quantity:
                    prod - quantity
                else:
                    prod.stock = 0
                return
