# random numbers!

import random
import numpy as np

number = random.randint(1, 20)
print (number)

ListOfRandomNumbers = []
for i in range(100):
    n = random.randint(1,20)
    ListOfRandomNumbers.append(n)

print(ListOfRandomNumbers)

list2 = [random.randint(1, 20) for i in range(100)]
print (list2)
print("length of list2 is", len(list2))

total = 0
for number in ListOfRandomNumbers:
    total = total + number
#
totalsum = sum(ListOfRandomNumbers)
print("total: ", total, totalsum)

# npnumber = np.random.