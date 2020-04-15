#day one Advent of code: takes a list of numbers and in part 1 adds them all together
#in part the proram looks for the number that appears twice first while adding two frequencies together,
# then the next one, then the next one and so on

import numpy as np
from itertools import cycle

frequencies = np.genfromtxt("C:/Users/schol/PyCharm Projekte/AdventofCode/AdventofCode_01_freq.txt", "int")
#test frequencies
#frequencies=[-6,3,8,5,-6]


#part one
start_f=0
for item in frequencies:
        start_f+=int(item)

print(start_f)

#part two
first_frequencies=set([])
current_f=0

for item in cycle(frequencies):
     if current_f in first_frequencies:
        break
     else:
        first_frequencies.update([current_f])
        current_f+=int(item)

print(current_f)

