input_1 = 'Python is a case sensitive language'
# a. finding length using len function
print(len(input_1))
# b. reversing string using slice syntax
print(input_1[::-1])
# c. slicing the input string and storing it in x
x = input_1[9:26]
print(x)
# d. usign replace function
x = x.replace('a case sensitive', 'object oriented')
print(x)
# e. 
index = input_1.find('a')
print(index)
# d. to remove white spaces we remove ' ' with '' with replace function
print(input_1.replace(' ', ''))
