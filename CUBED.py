#type a number
import math
while True:
    number=input("type a number: ")
    try:
        new_number= math.pow(float(number),3)
        print (new_number)
    except ValueError:
        print("please type an integer")
