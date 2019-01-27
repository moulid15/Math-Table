import math
import pandas
trig=dict={}
t2={}
table=[]
values=[]
keys=[]
for i in range(0,360):
    t2["sin("+str(i)+u'\xb0'+")"]=math.sin(i)
    t2["cos("+str(i)+u'\xb0'+")"]=math.cos(i)
    t2["tan("+str(i)+u'\xb0'+")"]=math.tan(i)
    values.append(t2)
    trig[str(i)+u'\xb0']=t2
    t2={}
    table=pandas.DataFrame(values,values[i],values[i])
    
print(table)
