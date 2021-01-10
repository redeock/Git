numbers = [1,2,3]
length = len(numbers)
i = 0
while i < length:
    print(numbers[i])
    i = i+1
#
sizes = [33,35,34,37,32,35,39,32,35,29]
for i, size in enumerate(sizes):
    if size == 32:
        print("The pants with size 32 are {}th.".format(i+1))
        break
#
list = [1,2,3,5,7,2,5,237,55]
for val in list:
    if val%3==0:
        print(val)
        break
#
numbers = [(1,2),(10,0)]
for a,b in numbers:
    if b == 0:
        print("It can not be devided with 0.")
        continue
    print("{}/{}={}".format(a,b,a/b))
#
