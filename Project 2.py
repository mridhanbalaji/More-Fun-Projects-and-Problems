from ast import Break
from audioop import add
from calendar import c
from multiprocessing.connection import wait
from pickle import APPEND

userValue =  200
a, b = 0, 1
fibonaccinumber = 0
Sum = 0

if userValue <= 0:
    print("Error")

else:
    for i in range (0, 200):
        # print(fibonaccinumber)
        fibonaccinumber = a + b
        a = b
        b = fibonaccinumber 
        if fibonaccinumber < 4000000 and fibonaccinumber % 2 == 0:
            Sum += fibonaccinumber


print(Sum)

# fibonaccinumber =  [i for i in fibonaccinumber if i % 2 == 0]
# print(newfibonaccinumber)
            
#if fibonaccinumber % 2 == 0:
    #list(newfibonaccinumber)
#print(newfibonaccinumber)
#print(fibonaccinumber)
#evenfibonaccinumber = [i for i in fibonaccinumber if fibonaccinumber % 2 == 0]
