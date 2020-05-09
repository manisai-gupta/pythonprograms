name1=input("enter the first name:").lower()
name2=input("enter the second name:").lower()
name1=name1.replace(" "," ")
name2=name2.replace(" "," ")
print(name1)
print(name2)
for i in name1:
    for j in name2:
        if(i==j):
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
print(name1)
print(name2)
count=len(name1+name2)
print(count) 
if(count>0):
    list=["friends","love","affection","marriage","enimes","siblings"]
    while len(list)>1:
        c=count%len(list)
        s_index=c-1
        if s_index>=0:
            left=list[:s_index]
            right=list[s_index+1:]
            list=right+left
        else:
            list=list[:len(list)-1] 
    print("the relation is:",list[0])
else:
    print("enter the different names")   

