# Math-Table
This is a math cheat sheet for multiplication tables,trig functions,etc

example for 0-3 degrees
       
       
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
          
