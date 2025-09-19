from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product = Product(None, 'Carrotes', 'Super C', 2.99)
    dao.insert(product)
    product = Product(None, 'Pommes', 'IGA', 3.49)
    dao.insert(product)
    product = Product(None, 'Bananes', 'Metro', 1.99)
    dao.insert(product)
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Fraises', 'Dollarama', 4.99)
    dao.insert(product)
    product_list = dao.select_all()
    brands = [u.brand for u in product_list]
    assert product.brand in brands

def test_product_update():
    product = Product(None, 'Biscuits', 'Pharmapprix', 5.99)
    assigned_id = dao.insert(product)
    corrected_brand = 'Pharmaprix'
    product.id = assigned_id
    product.brand = corrected_brand
    dao.update(product)
    product_list = dao.select_all()
    brands = [u.brand for u in product_list]
    assert product.brand in brands

def test_product_delete():
    product = Product(None, 'Fraises', 'Dolarama', 4.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    product_list = dao.select_all()
    prices = [u.price for u in product_list]
    assert product.price not in prices