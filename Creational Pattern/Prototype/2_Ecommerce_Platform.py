import copy


class Product:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price

    def clone(self):
        return copy.deepcopy(self)


class EcommercePlatform:
    def __init__(self):
        self.product_prototype = dict()

    def register_prototype(self, name, obj):
        self.product_prototype[name] = obj

    def create_product(self, key, **product_attr):
        product = self.product_prototype.get(key)
        if product:
            new_product = product.clone()
            new_product.category = product.category
            new_product.__dict__.update(product_attr)
            return new_product


if __name__ == "__main__":
    ecommerce = EcommercePlatform()

    product_category_1 = Product("Clothing", "USPA Shirt", 100)
    product_category_2 = Product("Electronics", "Samsung Mobile", 500)

    ecommerce.register_prototype("clothing", product_category_1)
    ecommerce.register_prototype("electronics", product_category_2)

    new_product_1 = ecommerce.create_product("clothing", name="T-Shirt", price=10)
    new_product_2 = ecommerce.create_product("clothing", name="Jeans", price=15)
    new_product_3 = ecommerce.create_product("electronics", name="I-Phone", price=600)
    new_product_4 = ecommerce.create_product(
        "electronics", name="Apple Watch", price=490
    )
