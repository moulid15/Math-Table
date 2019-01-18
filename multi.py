

table={}
t={}
for i in range(0,12):
    for j in range(0,12):
        t[j]=j*i
    table[i]=t
    t={}
print(table)

