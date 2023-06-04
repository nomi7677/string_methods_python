### How to make input = [1095, 1094, 1095] as output = [1005, 1014, 1015]
# use Fibonacci series

input  = [1095, 1094, 1095]
diff = [90, 80, 80]
output = []

for i in range(len(diff)):
    difference = input[i] - diff[i]
    output.append(difference)
print(output)