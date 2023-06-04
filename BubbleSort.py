c=[42,12,7,1,3,2,8]
n=len(c)
k=0
for i in range(0,n-1):
    for j in range(0, n-i-1):
        if(c[j]>c[j+1]):
            c[j],c[j+1]=c[j+1],c[j]
            k=k+1
# print("number of unsorted numbers are",k)
print("Sorted array is",c)