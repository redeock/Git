days_in_month = {
'January':31,
'February':28,
'March':31}
print(days_in_month)
#
dict={"Name tag":[1,2,3]}
print(dict["Name tag"])
#
days_in_month["February"]=29
print(days_in_month)
#
days_in_month={
'January':31,
'February':28,
'March':31,
'April':30,
'May':31}
for key in days_in_month.keys():
    print(key)
# key=이름표, value=값
for key, value in days_in_month.items():
    print("There are {} days in {}.".format(value,key))
#
def check_and_clear(box):
    print("If there is a defect, clear the box.")
    if "defect" in dict.keys():
        dict.clear()
    else:
        return(check_and_clear)

box1 = {"defect":10}
check_and_clear(box1)
print(box1)

box2 = {"normal":10}
check_and_clear(box2)
print(box2)
#
products = {"water_glue":800,"glue":1200,"color_paper":1000,"crayon":5000,"sketchbook":3500}
catalog = {"winter_shoes":12000, "butterfly_net":8000, "glue":1400}

products.update(catalog)
print(products)
#
tuple1 = (1,2,3)
tuple2 = 1,2,3
list3 = [1,2,3]
tuple3 = tuple(list3)

if tuple1 == tuple2 == tuple3:
    print("tuple1, tuple2 and tuple are all same.")
#
tuple4 = (11,22,33)
for i in range(len(tuple4)):
    print(tuple4[i])
# packing = 하나의 변수에 여려개의 값을 넣는 것
x=3
y=5
position = (x,y)
print("The value of position composed with x,y is {}.".format(position))
# unpacking = 패킹된 변수에서 여러개의 값을 꺼내오는 것
a=1
b=2
a,b = b,a
print("a :{}, b :{}".format(a,b))
#
products = {"glue":800, "color_paper":1000}
for product_detail in products.items():
    print("The price of {} : {} won".format(*product_detail))
# tuple을 return할 때는 *를 사용
