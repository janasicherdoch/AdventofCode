#this code takes a list of claims to a piece fabric
# such as #1 @ 1,3: 4x4 (first claim: 1 inch from left and 3 inches from the top, size: width=4 inches, height = 4 inches)
# and determins on how many square inches two or more claims overlap

import numpy as np

with open("AdventofCode_03_fabrics.txt", "r") as f:
    #strip the newline character
    fabrics = list(line[:-1] for line in f.readlines())
#print(fabrics)

#split one claim into 5 integers (Danke Martin!)
def split_claim_into_int(claim):
    id_claim, rest = claim.split("@")
    id_claim = int(id_claim.lstrip("#"))
    offset, rest = rest.split(":")
    x0, y0 = offset.split(",")
    x0 = int(x0)
    y0 = int(y0)
    width, height = rest.split("x")
    width = int(width)
    height = int(height)
    return(id_claim, x0, y0, width, height)

#create numpy array from integer claims
fabrics_int=np.array(list(split_claim_into_int(claims) for claims in fabrics))

#print(fabrics_int[0:3])

#determine size of fabric by finding x_min, x_max and y_min and y_max
#find x min und max
x_values=set([])
y_values=set([])
for i in range(len(fabrics_int)):
    x_value = fabrics_int[i,1]+fabrics_int[i,3]
    x_values.update([x_value])
    y_value = fabrics_int[i,2]+fabrics_int[i,4]
    y_values.update([y_value])

x_max = max(x_values) #x_max=1000
x_min = min(x_values) #x_min=22

y_max = max(y_values) #y_max=999
y_min = min(y_values) #y_min=11

#create array of zeros with size of fabric
fabrics_overlap = np.zeros((y_max, x_max), int)

#add one for every claim on inch of fabric and count the ones greater one to get the number of overlapping inches

for line in range(len(fabrics_int)):
    for i in range(fabrics_int[line,2], fabrics_int[line,2]+fabrics_int[line,4]):
        for j in range(fabrics_int[line,1], fabrics_int[line,1]+fabrics_int[line,3]):
            fabrics_overlap[i, j]+=1

overlap = np.sum(fabrics_overlap>1)
print(overlap)



#create smaller fabric for test, size 8x8

fabrics_testsize = np.zeros((8,8), int)
fabrics_claims_test = np.array([[1, 1, 3, 4, 4],
                                [2, 3, 1, 4, 4],
                                [3, 5, 5, 2, 2]])

for line in range(len(fabrics_claims_test)):
    for i in range(fabrics_claims_test[line,2], fabrics_claims_test[line,2]+fabrics_claims_test[line,4]):
        for j in range(fabrics_claims_test[line,1], fabrics_claims_test[line,1]+fabrics_claims_test[line,3]):
            fabrics_testsize[i, j]+=1

overlap_test = np.sum(fabrics_testsize>1)


print(fabrics_testsize)
print(fabrics_claims_test)
print(overlap_test)
print(len(fabrics_int))

