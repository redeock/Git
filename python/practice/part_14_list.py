def safe_index(my_list, value):
    if value in my_list == True:
        return print(my_list.index(value))
    else:
        return None

print(safe_index([1,2,3,4,5],5))
print(safe_index([1,2,3],5))
#
list1 = [1,2,3,4]

list1.insert(0,8)
print("The first valuse : {}".format(list1))

list1.sort()
print(list1)

list1.reverse()
print(list1)
#
str = "Today is cloudy"
words = str.split(' ')
#print(words)
position = words.index("cloudy")
words[position] = "sunny"
#print(position)
new_str = ' '.join(words)
print(new_str)
#
rainbow=['red','orange','yellow','green','blue','navy','purple']
red_colors = rainbow[0:3]
blue_colors = rainbow[4:7]
print(red_colors)
print(blue_colors)
#
def substring(text,start,end):
    return text[start:end]
my_text = 'Hello world'
between_2_5 = substring(my_text,2,5)
print(between_2_5)
#slice
"""
list1 = list(range(20))
new_list = list1[4,13,3]
print(new_list)
reverse_list = list[-4,-16,4]
print(reverse_list)
"""
list1 = [0,1,2,3,4,5]
list1[1:4] = [11,22,33]
print(list1)
list2 = [0,1,2,3,4,5]
del list2[1:4]
print(list2)
