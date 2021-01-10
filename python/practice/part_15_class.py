my_list = [1,2,3]
my_dict = {"glue" : 800,"crayon" : 3000}
my_tuple = (1,2,3)
number = 10
real_number = 3.14

print(type(my_list))
print(type(my_dict))
print(type(my_tuple))
print(number)
print(real_number)
#
list1 = [1,2,3]
list2 = [1,2,3]

if list1 is list1:
    print("list1 and list1 are same")
if list1==list2:
    print("list1 and list2 are same")
    if list1 is list2:
        print("And list1 and list2 are same instance")
    else:
        print("However, list1 and list2 are differnet instance")
#
list1 = list(range(10))
list2 = [1,2,3]
if isinstance(list1,list) and isinstance(list2,list):
    print("list1 and list2 were list class.")
# 인스턴스가 특정 클래스의 인스턴스인지 알아보는 방법
class Car():
    '''Vehicle'''
    def run(self):
        print("{} runs.".format(self.name))

taxi = Car()
taxi.name = 'TAXI'
taxi.run()
#
class Human():

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "{} (weight {}kg).format(self.name, self.weight)"

    def eat(self):
        self.weight += 0.1
        print("{} eats and becomes {}kg".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} walks and become {}kg".format(self.name, self.weight))

person = Human("human",60.5)
print(person.name)
print(person.weight)
#사람이 두번 걷고 한번 먹는 메소드 실행..?
