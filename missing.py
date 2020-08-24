print("Enter the random  elements from 1 to 10  to find missing elemts from them...")
print("How many elements you want to enter:")
n=int(input())
s1={i for i in range(1,11)}
s2=set()
for i in range(n):
    number=int(input())
    s2.add(number)
print(s1.difference(s2))

    
    