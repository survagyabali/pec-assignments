num_H=int(input('Number of Hydrogen atoms:'))
num_C=int(input('Number of Carbon atoms:'))
num_O=int(input('Number of Oxygen atoms:'))
#multiplying weight (grams/mole) by 100000 to avoid float point value errors 
w_H=100794
w_C=1201070
w_O=1599940
weight_p_mole=(w_H*num_H+w_C*num_C+w_O*num_O)/100000
print(weight_p_mole)4