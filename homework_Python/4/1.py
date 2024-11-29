class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock
        print ("Продукт создан:", self.__dict__)

    def update_stock(self, quantity: int):
        print (f"\nОбновление остатка у товара {self.name}.")
        if self.stock + quantity < 0:
            print ("    Ошибка. Остаток товара не может быть отрицательным.")
            print ("    Актуальный остаток:", self.stock)
            print (f"    Попытка списать: {quantity}")
        else:
            self.stock = self.stock + quantity
            print (f"    Изменение остатока: {quantity}")
            print ("    Актуальный остаток:", self.stock)


class Order:
    def __init__(self) -> None:
        self.products = {}
        print ("Заказ создан:", self.__dict__)
    
    def add_product(self, product: Product, quantity: int):
        self.products[product] = quantity
        print (f"   В заказ добавлен товар: {product.name} - {quantity} шт")

    def calculate_total(self) -> float:
        total = 0
        for product, quantity in self.products.items():
            total += product.price * quantity
        print ('Сумма заказа : ', total, 'руб.')
        return total

class Store:
    products: list[Product] = []
    def __init__(self, store_name: str) -> None:
        self.store_name = store_name
        print ("Магазин создан:", self.__dict__, "\n")

    def add_product(self, product: Product):
        self.products.append(product)
        print (f"\nНа склад добавлен товар: {product.name} [{product.stock} шт по {product.price} руб.]")

    def list_products(self):
        print ("\nСписок товаров на складе:")
        for product in self.products:
            print (f"  {product.name}  {product.price}  {product.stock}")

    def create_order(self):
        print ("\nСоздан заказ на складе")
        return Order()            


def main():
    s = Store('Склад №5')

    p1 = Product("Ноутбук", 1000, 5)
    p2 = Product("Смартфон", 500, 10)

    p1.update_stock(-3)
    p2.update_stock(-30)  

    s.add_product(p1)
    s.add_product(p2)

    o = s.create_order()

    o.add_product(p1, 2)
    o.add_product(p2, 3)

    o.calculate_total()

    s.list_products()

if __name__ == "__main__":
    main()
