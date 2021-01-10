try:
    a=3/0
except:
    print("You can not devide with 0.")
#
try:
    a=5
    b=0
    c=a/b
except Exception as ex:
    print('Here is an error : {}'.format(ex))
#
shops = {
"A shop" : {"Scissors" : 500, "Crayon" : 3000},
"B shop" : {"glue" : 800, "paper" : 300, "A4" : 8000},
"C shop" : {"glue" : 500, "bond" : 2000, "flower pot" : 3000}
}

for shop, products in shops.items():
    for product, price in products.items():
        if product == 'glue':
            print("{} : {} won".format(shop,price))
#
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
                raise StopIteration

except StopIteration:
    print('Error')
