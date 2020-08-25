# print("Enter the random  elements from 1 to 10  to find missing elemts from them...")
# print("How many elements you want to enter:")
# n=int(input())
# s1={i for i in range(1,11)}
# s2=set()
# for i in range(n):
#     number=int(input())
#     s2.add(number)
# print(s1.difference(s2))

def missing(arr,n):
    sum_n=((n+1)*(n+2))/2
    # print(sum_n)
    sum_user=0
    for i in range(n):
        sum_user+=arr[i]
    print(sum_n-sum_user)
    
print("How many elements you want to enter:")
n=int(input())
l=[]
for i in range(n):
    number=int(input())
    l.append(number)
n=len(l)
# print(n)
missing(l,n)



    
    