from datetime import datetime

hour = datetime.now().hour

if hour<12:
    print('It is mornning.')
    print(hour)
#
number = 15
if number % 3 == 0:
    print("{} is a multiple of 3.".format(number))

number = 16
if number % 3 == 0:
    print("{} is a multiple of 3.".format(number))
#
from datetime import datetime
hour = datetime.now().hour

if hour%6==0:
    print('A bell is ringing.')
#
mine = 'scissors'
yours = 'rock'
if mine == yours:
    print("Draw")
else:
    print("Not draw")
#
gender = "Man"
if gender == "Man":
    print("It is a man.")
elif gender == "Woman":
    print("It is a woman.")
else:
    print("It is a non-binary.")
#
    
