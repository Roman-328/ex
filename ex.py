from abc import ABC, abstractmethod


class Item_Menu(ABC):
    def __init__(self, name:str, price:float):
        self.name=name
        self.price=price

    def info(self):
        pass


class Drink(Item_Menu):
    def __init__(self, name:str, price:float, size:str):
        super().__init__(name, price)
        self.size=size

    def info(self):
        print(f"Drink:{self.name}({self.size})-${self.price:.2f}")


class Dessert(Item_Menu):
    def __init__(self, name:str, price: float):
        super().__init__(name, price)
    
    def info(self):
        print(f"Dessert:{self.name}-{self.price:.2f}")

class Order:
    def __init__(self, order_n: int, table:int):
        self.order_n= order_n
        self.table= table
        self.items=[]
    
    def add_item(self, item:Item_Menu):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)
    
    def order_info(self):
        print(f"Order number:{self.order_n}, Table:{self.table}")
        print("Items:")
        for item in self.items:
            item.info()
        print(f"Total: ${self.total():.2f}")
        print('-'*10)


class Manage:
    def __init__(self):
        self.orders=[]
        self.n_order=1

    def CreateOrder(self, table_n:int):
        order = Order(self.n_order, table_n)
        self.orders.append(order)
        self.n_order += 1
        return order
    def order_find(self, order_n:int):
        for order in self.orders:
            if order.order_n == order_n:
                return order
            raise Exception(f"Order number {order_n} not found")
    
    def all_orders(self):
        print("All Orders:")
        for order in self.orders:
            order.order_info()



vodka= Drink("Vodka", 3, "stopka")
gin= Drink("London Dry Gin", 4, "stopka")
pickle= Dessert("Pickle", 0.5)
print("Drink list: Vodka n1, Gin n2")
print("Dessert list: Pickle n1")


order_manage=Manage()

order= order_manage.CreateOrder(table_n=1)
print("Drink:")
d= int(input())
if d ==1:
    order.add_item(vodka)
else:
    order.add_item(gin)
ds= int(input())
if ds ==1:
    order.add_item(pickle)
order.order_info()

order_manage.all_orders()

