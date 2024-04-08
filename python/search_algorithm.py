# 7.      BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.

# Define a function
def binary_recur(arr, start, end, num):
    if end >= start:
        
        # split arr into two
        mid = start + end - 1 // 2
        
        # search through the first half
        if arr[mid] < num:
            binary_recur(arr, mid+1, end, num)
           
        # search through the other half 
        elif arr[mid] > num:
            return binary_recur(arr, start, mid-1, num)
        
        else:
            return mid
    
    else:
        
        return -1
    

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Type in a number between 1 - 10: " ))

# if number is greater than 10 or less than , quit 
if  num <= 0 or num > 10:
    print("Please type in a number between 1 - 10")
    quit()

else:
    result = binary_recur(arr, 0, len(arr) - 1, num)

    if result != -1:
        print("The number is present at index", str(result))
    else:
        print("The number is not present in the option")
    


    
    
