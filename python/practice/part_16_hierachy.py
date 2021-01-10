class Car():
    def run(self):
        print("A car runs.")

class Truck(Car):
    def load(self):
        print("Cargo loaded")
# Car = parent, Truck = child
class Truck(Car):
    def run(self):
        print("A truck runs")
# override = 덮어쓰기 = 내용 바꾸기
# car에서 정의된 run을 자식 클래스인 truck에서 덮어쓰기 함
class Truck(Car):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
# name은 부모에게서 super()함수로 가져오고, 새 변수를 입력받음
class MyException:

shops = {
"A shop" : {"Scissors" : 500, "Crayon" : 3000},
"B shop" : {"glue" : 800, "paper" : 300, "A4" : 8000},
"C shop" : {"glue" : 500, "bond" : 2000, "flower pot" : 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == 'glue':
                print("{} : {} won".format(shop,price))
                raise MyException
except MyException:
    print("We find a glue.")
