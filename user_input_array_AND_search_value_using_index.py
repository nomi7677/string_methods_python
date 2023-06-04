from array import *
arr = array('i', ())
n = int(input("Enter the length of array: "))

for i in range(n):
    x= int(input("enter the value for array"))
    arr.append(x)

print(arr)