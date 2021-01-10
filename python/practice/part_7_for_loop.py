list=['scissors','rock','paper']
for list in list:
    print(list)
#
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
#
for i in range(4):
    print(i)
#
rainbow=['red','orange','yellow','green','blue','navy','purple']
for i in range(len(rainbow)):
    color = rainbow[i]
    print('The {}th color is {}'.format(i+1,color))
#
days=[31,29,31,30,31,30,31,31,30,31,30,31]
for i, day in enumerate(days):
    day = days[i]
    print("The days of {} is {}.".format(i+1,day))
# enumerate : 열거하다
