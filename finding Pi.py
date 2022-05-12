import random
import numpy as np
import matplotlib.pyplot as plt


def estimatepi(number):
    estimateinrange = 0
    totalestimates = 0
    _listx = []
    _listy = []
    for _ in range(number):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance < 1:
            estimateinrange += 1
        totalestimates += 1
        _listx.append(x)
        _listy.append(y)
        _listx = [int(i) for i in _listx]
        _listy = [int(i) for i in _listy]
        plt.scatter(_listx, _listy, label= "stars", color= "green", marker= "*", s=30)
    

    

       

    
    

    _pi = 4 * estimateinrange/totalestimates
    
    
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("The Estimates of pi")
    plt.show()
    return _pi

estimatepi(10)

    

   
