


import random
import math
import time

  

def space_chooser():
    spaces = 20
    car_interval = random.randint(5,10)
    for i in range(20):
    #while True:
        car = 0
        randomSpace = random.randint(1,20)
        indiv_space = 'Slot', str(randomSpace)
        give_space = print(f'Your parking slot is {indiv_space}')
        spaces -= 1
        print('There are', spaces, ' slots left in the parking lot')
        time.sleep(car_interval)
        car += 1
         
        #if spaces == 15:
        if spaces == 0:
            print('There are no more spaces in the parking lot')
        #break
        

space_chooser()

