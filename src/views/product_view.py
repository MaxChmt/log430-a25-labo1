"""
product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste des produits\n2. Ajouter un produit\n3. Supprimer un produit\n4. Mettre à jour un produit\n5. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)
            elif choice == '3':
                product_id = ProductView.get_selected_id()
                controller.delete_product(product_id)
            elif choice == '4':
                product_id = ProductView.get_selected_id()
                newName, newBrand, newPrice = ProductView.get_inputs()
                product = Product(product_id , newName, newBrand, newPrice)
                controller.update_product(product)
            elif choice == '5':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{product.id}: {product.name} {product.price} ({product.brand})" for product in products))

    @staticmethod
    def get_inputs():
        """ Prompt product for inputs necessary to add a new product """
        name = input("Nom du produit : ").strip()
        brand = input("Marque du produit : ").strip()
        price = input("Prix du produit : ").strip()
        return name, brand, price
    
    @staticmethod
    def get_selected_id():
        """ Prompt product for input necessary to select an existing product """
        product_id = input("Id du produit : ").strip()
        return product_id