"""
Generating random numbers between 1 qand 20
based on random number, we will classify by range
>15 = cherries
>5 = plum
>2 = melon
>1 Bell
if none, = bar
Will loop 3 times
"""

"""
import random
num = generate random number 

    greater than 15, 
    then the result will be "Cherries"
    if num is > 10, 
    then the result will be "Orange"
    if num is > 5, 
    then the result will be "Plum"
    if num is > 2, 
    then the result will be "Melon"
    if num is > 1, 
    then the result will be "Bell"
    if none
    result is BAr

    loop three times
    print the output 
"""
import random

def main():
    for i in range(0, 3):
        spin()

def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if(rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "Orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Bell"
    elif(rand_num > 1):
        output = "Melon"
    else:
        output = "Bar"
    
    print(output, end=" ")

main()