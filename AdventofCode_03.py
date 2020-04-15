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

print(fabrics_int)


