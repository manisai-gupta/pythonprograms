# l=[1,2,3,4,5,6]
# n=len(l)
# k=6
# s=set()
# for i in range(n):
#     for j in range(0,n//2):
#         if k is i+j:
#             s.add((i,j))
#             print("The sum of target elements are ({},{})".format(i,j))
# print(s)


# l1=[-1,1,5,7,2,3]
# n=len(l1)
# print("Enter the target element:")
# k=int(input())
# l2=[]
# for i in range(0,n):
#     a=l1.pop()
#     b=k-a
#     if b in l1:
#         l2.append((a,b))
# print(l2)


l1=[-1,1,5,7,2,3]
n=len(l1)
print("Enter the target element:")
target=int(input())
d=dict()
for i, num in enumerate(l1):
    n = target - num
    if n not in d:
        d[num] = i
    else:
        print([n, num])








    