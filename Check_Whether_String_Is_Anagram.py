def check(str1, str2):
    if (sorted(str1) == sorted(str2)):
        print("String is anagram")
    else:
        print("String is not anagram")
str1 = "study"
str2 = "dusty"

check(str1,str2)