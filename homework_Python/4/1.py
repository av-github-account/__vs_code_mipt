# НАХОЖУСЬ В КОМАНДИРОВКЕ
# Авраменко Алексей
# Доделаю до 01 ноября 23:59


class Product:
    "Класс для товара"
    def __init__(self, name, price, stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock
        print ("Продукт создан:", self.__dict__)

    def update_stock(self, quantity):
        print ("\nОбновление остатка.")
        if self.stock - quantity < 0:
            print ("    Ошибка. Остаток товара не может быть отрицательным.")
            print ("    Актуальный остаток:", self.stock)
            print (f"    Попытка списать: {quantity}")
        else:
            self.stock = self.stock - quantity
            print (f"    Изменение остатока: минус {quantity}")
            print ("    Актуальный остаток:", self.stock)

class Order:
    "Класс для заказа"
    def __init__(self) -> None:
        self.products = {}
        print ("\nЗаказ создан:", self.__dict__)
    
    def add_product(self, product, quantity):
        self.products [product] = quantity 
        print (f"\nВ заказ добавлен товар: {product} - {quantity}")

    def calculate_total(self):
        total = 0
        print (f"\nПодсчет суммы заказа Total:")
        for item in self.products.keys():
            qnt = self.products.get(item)
            prc = 1 #как найти цену конкретного товара?
            total += qnt*prc
        print ('Total = ', total)

class Store:
    "Класс для Склада"
    def __init__(self, store_name) -> None:
        self.store_name = store_name
        print ("Магазин создан:", self.__dict__)

    def add_product(self, product, quantity):
        # self.products [Product.name] = Product.stock
        # print (f"\nНа склад добавлен товар: {product} - {quantity}")
        pass
    def list_products(self):
        pass

    def create_order(self):
        pass




p1 = Product("Ноутбук", 1000, 5)
p2 = Product("Смартфон", 500, 10)
p3 = Product("Телевизор", 2000, 15)

o1 = Order()
o2 = Order()

S = Store("Склад №5")
# S.add_product (p1, 10)
# S.add_product (p2, 20)
# S.add_product (p3, 30)

p1.update_stock(2)
p3.update_stock(20)

o1.add_product ("Ноутбук", 1)
o1.add_product ("Смартфон", 2)
o1.calculate_total ()

# print(o1.products)
# print(type(o1.products))
# print ("!!!!!", p1.name)














# p2 = Product("Смартфон", 500, 10)


# нет, ты создаешь заказ order = store.create_order()
# потом добавляешь товары order.add_product(product, 10)



# print(p1.__dict__)
# print(p2.price)
# print(p1())
# print(p1.__dict__)
# print(p1.__doc__)

# product1 = Product("Ноутбук", 1000, 5)
# print (Product.product1)
# product1.__dict__

# # Задача: Модель магазина

# ## Пример использования

# ```python
# # Создаем магазин
# store = Store()

# # Создаем товары
# product1 = Product("Ноутбук", 1000, 5)
# product2 = Product("Смартфон", 500, 10)

# # Добавляем товары в магазин
# store.add_product(product1)
# store.add_product(product2)

# # Список всех товаров
# store.list_products()

# # Создаем заказ
# order = store.create_order()

# # Добавляем товары в заказ
# order.add_product(product1, 2)
# order.add_product(product2, 3)

# # Выводим общую стоимость заказа
# total = order.calculate_total()
# print(f"Общая стоимость заказа: {total}")

# # Проверяем остатки на складе после заказа
# store.list_products()
# ```
