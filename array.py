from array import *
values = array('i', [12,14,2,3,5,19])
# values.reverse()
# print(values)

# new array assigning values from old array
newArr = array(values.typecode,(a for a in values))
for e in newArr:
    print(e)

