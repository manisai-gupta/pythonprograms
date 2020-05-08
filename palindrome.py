s1=input("enter the name")
s2=""
strcpy(s2,s1)
strrev(s2)
if(strcmp(s2,s1)==0):
    print("it is a palindrome",s2)
else:
    print("its not palindrome")
