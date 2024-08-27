from producto import Product
from tienda import Restaurant, Supermarket, Pharmacy

def create_store():
    store_type = input("Enter the type of store (Restaurant, Supermarket, Pharmacy): ")
    name = input("Enter the name of the store: ")
    delivery_cost = float(input("Enter the delivery cost: "))

    if store_type == "Restaurant":
        return Restaurant(name, delivery_cost)
    elif store_type == "Supermarket":
        return Supermarket(name, delivery_cost)
    elif store_type == "Pharmacy":
        return Pharmacy(name, delivery_cost)

def add_product(store):
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the product stock: "))
    product = Product(name, price, stock)
    store.add_product(product)

def main():
    store = create_store()

    while True:
        print("\n1. Add product")
        print("2. List products")
        print("3. Make sale")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            add_product(store)
        elif option == "2":
            print(store.list_products())
        elif option == "3":
            product_name = input("Enter the product name to sell: ")
            quantity = int(input("Enter the quantity: "))
            store.make_sale(product_name, quantity)
        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
