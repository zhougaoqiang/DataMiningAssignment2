def nestLoop(number):
    sum = 0
    for i in range(number) :
        for j in range(number) :
            sum += 10
    return sum

######num = number ** 2
def singleLoop(num):
    sum = 0
    for i in range(num) :
        sum += 10
    return sum

def callOtherFunction(num) :
    sum = 0
    for i in range(num):
        sum += singleLoop(num)
    return sum

import time

cal = 10000
calForSingle= cal ** 2
startTime = time.time()
sum = nestLoop(cal)
print(f'sum={sum}, time={time.time()- startTime}')

startTime = time.time()
sum = singleLoop(calForSingle)
print(f'sum={sum}, time={time.time()- startTime}')

startTime = time.time()
sum = callOtherFunction(cal)
print(f'sum={sum}, time={time.time()- startTime}')