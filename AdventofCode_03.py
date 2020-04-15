import numpy as np

fabrics = np.genfromtxt("C:/Users/schol/PyCharm Projekte/AdventofCode/AdventofCode_03_fabrics.txt",
                        dtype = None,
                        comments = None,
                        delimiter =(' ') )


def create_int_array(input_array):
    new_array = []
    for n in range(len(input_array)):
      element = input_array[n]
      element_2 = element[2]
      element_3 = element[3]
      index = n
      pos_x = element_2[:3]
      pos_y = element_2[4:7]
      size_x = element_3[:2]
      size_y = element_3[3:]
      new_element = [index, pos_x, pos_y, size_x, size_y]
      new_array.append(new_element)
    return new_array

fabrics_int = np.array(create_int_array(fabrics))
print(fabrics_int)
print(fabrics_int[0, :])
fabrics_size = np.size(fabrics_int)
fabrics_size_y= np.size(fabrics_int,0)
fabrics_size_x= np.size(fabrics_int,1)
print(fabrics_size, fabrics_size_y, fabrics_size_x)

print(int(fabrics_int[0,1])+int(fabrics_int[0,2]))