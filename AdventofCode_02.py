import numpy as np

product_ids = np.genfromtxt("C:/Users/schol/PyCharm Projekte/AdventofCode/AdventofCode_02_strings.txt", "str")
#print(product_ids)

# part one
count_2_total = 0
count_3_total = 0


def count_double(box_ID):
    count_2 = 0
    for letter in box_ID:
        if box_ID.count(letter) == 2:
            count_2 += 1
    if count_2 > 0:
        return True


def count_triple(box_ID):
    count_3 = 0
    for letter in box_ID:
        if box_ID.count(letter) == 3:
            count_3 += 1
    if count_3 > 0:
        return True


for item in product_ids:
    if count_double(item) is True:
        count_2_total += 1
    if count_triple(item) is True:
        count_3_total += 1

# print(product_ids[0])
# print(count_2_total)
# print(count_3_total)
print(count_2_total * count_3_total)


# part two

def check_number_of_different_letters(string1, string2):
    letter_count = 0
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            letter_count += 1
    return letter_count

def remove_different_letter(string1,string2):
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            string_new=string1.replace(string1[index],'')
    return string_new

def find_strings_with_one_different_letter(list_of_strings):
  for n in range(len(list_of_strings)):
      for product_id in list_of_strings:
          if check_number_of_different_letters(product_id, list_of_strings[n])==1:
              #print(product_id)
              #print(remove_different_letter(product_id, product_ids[n]))
              return product_id, list_of_strings[n]

strings= find_strings_with_one_different_letter(product_ids)
print(remove_different_letter(strings[0], strings[1]))



