# Draw a triangle pattern using hashes

for i in range (4):

    # using i+1 as it starts from 0

    for j in range(i+1):
        print("# ", end="")

    print()


################### Printing Triangle in reverse order ####################
print()
#######################

for i in range(4):
    for j in range(4-i):
        print("# ", end="")

    print()
