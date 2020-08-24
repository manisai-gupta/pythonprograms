l=[1,2,3,4,5,6]
n=len(l)
k=6
s=set()
for i in range(n):
    for j in range(0,n//2):
        if k is i+j:
            s.add((i,j))
            print("The sum of target elements are ({},{})".format(i,j))
print(s)