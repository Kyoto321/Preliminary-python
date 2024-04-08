from collections import Counter
from statistics import variance
import random

MONDAY = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
TUESDAY = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE"
WEDNESDAY = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE"
THURSDAY = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
FRIDAY = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"

WEEK = MONDAY + TUESDAY + WEDNESDAY + TUESDAY + FRIDAY
#print(WEEK)



# Get unique values ad save to python
str = WEEK
words = str.split(' ')
c = Counter(words)

COLOR = dict(c)
#print(COLOR)
#print(COLOR.values())


# ---------------------------------------------

# 1.     Which color of shirt is the mean color?

mean = round(sum(COLOR.values()) / float(len(COLOR))) 

mean_key = None
mean_val = None

for key, val in COLOR.items():

    if mean_val is None or val == mean_val:
        mean_val = val
        mean_key = key


print("The average color worn throughout the week is:", mean_key, mean)
# The average color worn throughout the week is: PINK, 6

# -------------------------------------------



# --------------------------------------------

# 2.      Which color is mostly worn throughout the week?

max = max(COLOR, key=COLOR.get)

print("The color mostly worn throughout the week is:", max)
#The color mostly worn throughout the week is: BLUE, 27

# ---------------------------------------------



# duplicate and string "WEEK" and convert to a list 
list = MONDAY + TUESDAY + WEDNESDAY + TUESDAY + FRIDAY
WEEKdpl = list.split(',')
#print(list)



# ------------------------------------------

# 3.      Which color is the median?

# to get the median in list "WEEKdpl"
def get_middle(var):
    mid = int(len(var)/2)
    if len(var) % 2 == 0:
        return var[mid-1:mid+1]
    else:
        return var[mid]
    
middle = get_middle(WEEKdpl)

print("The middle(normal) color is:", middle)
# The middle(normal) color is:  RED



# --------------------------------------------------

# 4.      BONUS Get the variance of the colors

sample = (COLOR.values())
var = round(variance(sample))
print("The variance is:", var)
# The variance is: 49

# ---------------------------------------------------



# ------------------------------------------------

# 5.      BONUS if a colour is chosen at random, what is the probability that the color is red?        

selected_item = random.choice(WEEKdpl)

if selected_item == "RED":
    prob = COLOR.get('RED,') / len(WEEKdpl)

print("Probability that the color RED", COLOR.get('RED,'), '/', len(WEEKdpl), '=', COLOR.get('RED,') / len(WEEKdpl))
# Probability that the color RED 9 / 91 = 0.0989010989010989

# ------------------------------------------------









   
        

        
        
        
        
        
        
        
        
    

#-------------------------- Rough Work ------------------- 

#unique = [w for w in words if c[w] == 1]

#print("Unique words: ", unique)

#numofBlue =  WEEK.count("BLUE")

#print(numofCounts)


# which color of shirt is mean color
"""
from statistics import mean 
import pandas as pd

#MONDAY = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]

data = pd.read_csv("table.csv")


print(data)

"""

"""

"""