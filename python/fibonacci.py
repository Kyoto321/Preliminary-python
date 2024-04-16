# 9.      Write a program to sum the first 50 fibonacci sequence.

# first 50 fibonacci sequence 

a, b = 0, 1
for i in range(0, 50):
    print(a)
    a, b = b, a + b
    
