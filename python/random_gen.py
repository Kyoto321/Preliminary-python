# 8.      Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random

min = 0
max = 1

# generate numbers

number = [random.randint(min, max) for x in range(4)]

num = str(''.join(map(str,number)))

print("Binary number is:", num)

# conver to base 10

def bin2dec(b): 
    return bin2dec(b[1::]) + int(b[0])*2**(len(b)-1) if len(b) > 1 else int(b)
 
bin = num
print(f"Base 10 value: {bin2dec(bin)}") 



