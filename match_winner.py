import csv
with open('matches.csv') as csv_file:
     matches = csv.reader(csv_file, delimiter=',')
     l=[]
     #line_c=0
     for row in matches:
         if row[10]!='winner':
           l.append(row[10])
     dict={s:l.count(s) for s in l}
     print(dict)
     key_list=list(dict.keys())
     val_list=list(dict.values())
     #finding max matches won by a team
     a=max(dict.values())
     print(key_list[val_list.index(a)],end="")
     print(a)