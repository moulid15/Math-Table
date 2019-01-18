import math
trig={}
t2={}
for i in range(0,360):
    t2["sin("+str(i)+")"]=math.sin(i)
    t2["cos("+str(i)+")"]=math.cos(i)
    t2["tan("+str(i)+")"]=math.tan(i)
    trig[str(i)+u'\xb0']=t2
    t2={}
print(trig)
