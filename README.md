# Math-Table
This is a math cheat sheet for multiplication tables,trig functions,etc

## Clone and Contribute
``` 
git clone https://github.com/moulid15/Math-Table.git
```

### Division
###### this is only for 0-10 but div.py has 0-225
```python
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
```
```
 0   1    2     3    4    5    6     7    8     9     10
0    0   0    0     0    0    0    0     0    0     0     0
1    0   1  1/2   1/3  1/4  1/5  1/6   1/7  1/8   1/9  1/10
2    0   2    1   2/3  1/2  2/5  1/3   2/7  1/4   2/9   1/5
3    0   3  3/2     1  3/4  3/5  1/2   3/7  3/8   1/3  3/10
4    0   4    2   4/3    1  4/5  2/3   4/7  1/2   4/9   2/5
5    0   5  5/2   5/3  5/4    1  5/6   5/7  5/8   5/9   1/2
6    0   6    3     2  3/2  6/5    1   6/7  3/4   2/3   3/5
7    0   7  7/2   7/3  7/4  7/5  7/6     1  7/8   7/9  7/10
8    0   8    4   8/3    2  8/5  4/3   8/7    1   8/9   4/5
9    0   9  9/2     3  9/4  9/5  3/2   9/7  9/8     1  9/10
10   0  10    5  10/3  5/2    2  5/3  10/7  5/4  10/9     1
```


### Trig functions
       
       
```python
import math
trig={}
t2={}
for i in range(0,360):
    t2["sin("+str(i)+u'\xb0'+")"]=math.sin(i)
    t2["cos("+str(i)+u'\xb0'+")"]=math.cos(i)
    t2["tan("+str(i)+u'\xb0'+")"]=math.tan(i)
    trig[str(i)+u'\xb0']=t2
    t2={}
print(trig)
  ```
 ```
{
  '0°': {'sin(0°)': 0.0, 'cos(0°)': 1.0, 'tan(0°)': 0.0}, 
  '1°': {'sin(1°)': 0.8414709848078965, 'cos(1°)': 0.5403023058681398, 'tan(1°)': 1.5574077246549023}, 
  '2°': {'sin(2°)': 0.9092974268256817, 'cos(2°)': -0.4161468365471424, 'tan(2°)': -2.185039863261519}, 
  '3°': {'sin(3°)': 0.1411200080598672, 'cos(3°)': -0.9899924966004454, 'tan(3°)': -0.1425465430742778}
}
```



          
