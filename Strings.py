name= "Nauman"
print(name) # prints whole string in variable
print(name[0]) # prints character at first index point
print(name[0:4]) # prints characters from 1st index till 3rd. stop argument is excluded
print(name[-3:6]) # starts from -3 i.e. -1 means last character
print(name[:]) # prints full string
print(name[:4]) # prints start(0) till 3rd index which is 4th character
print(name[2:]) # prints from 2nd index till last
print(name[1:6:2]) # prints from 1st index to 5th with gap of 1 i.e. amn
print(name[: : -1]) # prints backward
print(name[-1::-1]) # prints backward

#----------------- METHODS OF STRING --------------------

print(len(name)) # 6 ... counts characters

str = "NaUmaN"

print(str.lower()) # nauman
print(str.upper()) # NAUMAN
print(str.title()) # first character is upper case rest is lower
print(str.count("a")) # counts lower a from string

# --------------------- print length of name and count with case in-sensitive method

#str_name, chr = input("Please enter name and character you want to count from the name \n").split(",")
#print(f"Length of name is {len(str_name)}")
#print(f"count is {str_name.lower().count(chr.lower())}")

#--------------STRIP METHOD used to remove white spaces-----------
# lstrip() is used to remove left spaces and rstrip() for right
# dots is used to check the ......
str_name1 = "      Nauman     "
dots=".........."
print(str_name1+dots) #       Nauman     ..........
print(str_name1.lstrip()+dots)
print(str_name1.rstrip()+dots)
print(str_name1.strip()+dots) # both spaces are removed

# replace and find method in strings
str = "He is a beautiful dancer"
print(str.replace(" ", "_")) # He_is_a_beautiful_dancer
print(str.replace(" ", "_",1)) # only put _ for first whitespace






