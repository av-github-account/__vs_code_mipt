class InvalidStockValue(Exception):
    invalid_stock_value = None

    def __init__(self, invalid_stock_value):
        self.invalid_stock_value = invalid_stock_value


class InvalidQuantityValue(Exception):
    invalid_quantity_value = None

    def __init__(self, invalid_quantity_value):
        self.invalid_quantity_value = invalid_quantity_value


class ProductAlreadyInStore(Exception):
    product_name: str

    def __init__(self, product_name):
        self.product_name = product_name


class ProductOutOfStock(Exception):
    pass


class Product:
    def __init__(self, name: str, price: float, stock: int):
        self._name: str = name
        self._price: float = price
        self._stock: int = stock

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock: int):
        self.update_stock(stock=stock)

    def __str__(self) -> str:
        return f"{self._name}, price: {self._price}, stock={self._stock}"

    def __repr__(self) -> str:
        return f"{self._name}_{self._price}_{self._stock}"

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, product) -> bool:
        return isinstance(product, Product) and (
            self._name == product._name and self._price == self._price
        )

    def update_stock(self, diff: int):
        if self.stock + diff < 0:
            raise InvalidStockValue(diff)

        self._stock += diff


class Order:
    products: dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int):
        if quantity <= 0:
            raise InvalidQuantityValue(invalid_quantity_value=quantity)

        current_quantity = self.products.get(product, 0)

        try:
            product.update_stock(-quantity)
        except InvalidStockValue:
            raise ProductOutOfStock

        self.products[product] = current_quantity + quantity

    def calculate_total(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity

        return total_price


class Store:
    products: list[Product] = []

    def add_product(self, product: Product):
        if product not in self.products:
            self.products.append(product)

    def list_products(self):
        products = [str(product) for product in self.products]
        print("\n".join(products))

    def create_order(self):
        return Order()


def main():
    store = Store()

    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)

    store.add_product(product1)
    store.add_product(product2)

    store.list_products()

    order = store.create_order()

    order.add_product(product1, 2)
    order.add_product(product2, 3)

    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    # Проверяем остатки на складе после заказа
    store.list_products()


if __name__ == "__main__":
    main()
