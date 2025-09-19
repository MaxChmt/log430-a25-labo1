"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView 

if __name__ == '__main__':
    print("===== LE MAGASIN DU COIN =====")
    while True:
        print("\n1. Menu utilisateurs\n2. Menu produits")
        choice = input("Choisissez une option: ")
        if choice == '1':
            main_menu = UserView()
        elif choice == '2':
            main_menu = ProductView()
        else:
            print("Cette option n'existe pas.")
        main_menu.show_options()

