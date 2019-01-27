import pandas
table={}
t={}
table1=[]
for i in range(0,16):
    for j in range(0,16):
        t[j]=j*i
    table[i]=t
    t={}
    table1=pandas.DataFrame(table,table[i],table[i])
print(table1)
