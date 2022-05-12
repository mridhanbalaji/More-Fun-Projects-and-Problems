

from pickle import FALSE


x =  121
t = range(1, x)
y= [i for i in t if x % i == 0]

def is_prime_number(y):
    if y >= 2:
        for z in range(2,y):
            if not ( y % z):
                return False
    else:
	    return True
        

new_list = [i for i in y if is_prime_number(i) and i < x]

Final_list = new_list[-1:]

print(Final_list)





