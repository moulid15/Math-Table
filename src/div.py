import pandas
from fractions import Fraction
table={}
t={}
table1=[]
for i in range(0,225):
    for j in range(0,225):
        if i is 0:
            t[j]=0
        else:
            t[j]=str(Fraction(j/i).limit_denominator())
    table[i]=t
    t={}
    table1=pandas.DataFrame(table,table[i],table[i])
print(table1)
