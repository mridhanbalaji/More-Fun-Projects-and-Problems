       
from math import inf
from multiprocessing.dummy import Value
import numbers
from operator import truediv
from optparse import Values


a = 3
b = 5
multiplevalues = int
Sum1 = 0
Sum2 = 0

for i in range (0, 1000):
for multiplevalues in range(0 , 1000):
    Sum1 = a*multiplevalues
    Sum2 = b*multiplevalues
    Finalsum = Sum1 + Sum2

print(Finalsum)

multiplesof5 = [ i for i in range(1, 1001) if i % 5 == 0 ]
multiplesof3 = [i for i in range(1, 1001) if i % 3 == 0]

Sum1 = sum(multiplesof5)
Sum2 = sum(multiplesof3)
Finalsum = Sum1 + Sum2

print(Finalsum)

multiplevalues = (list(range (1, 1001)))

newlist = [i*5 for i in multiplevalues]

if Value(newlist) <=1001:
    Pedro = sum(Value(newlist))

Pedro = sum(i in range (1,1001) for i in newlist)
newnewlist = [i in range(1,1001) for i in newlist]

Finallist = [i is True for i in newnewlist]
    
print(Pedro)


Sum = 0

for i in range (1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        Sum += i

print(Sum)

x = int(input("What is your range:"))
var3 = list(range(3, x ,3))
var5 = list(range(5, x ,5))
Sumvar3 = sum(i for i in var3)
Sumvar5 = sum(i for i in var5) 
TotalSum = Sumvar3 + Sumvar5
print(TotalSum)

