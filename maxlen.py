def longestWordLength(string): 
    max="0"
    for i in string.split():
        print(i,len(i))
        if i > max:
          max=i
    return max
string = input()
print(longestWordLength(string)) 
  