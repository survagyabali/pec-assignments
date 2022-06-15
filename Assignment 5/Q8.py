list = []  #creating an empty list

#taking list input
for i in range(10):
    num = int(input('Enter 11 numbers:'))
    list.append(num)  
#A
print('Positive Numbers in list are:')
for i in list:
  if i>=0:
    print(i)
#B
print('Negative number in list:')
for i in list:
  if i<0:
    print(i)
#C
print('odd numbers in list:')
for i in list:
    if i % 2 != 0:
        print(i)
#D
print('even numbers in list:')
for i in list:
    if i % 2 == 0:
        print(i)
#E
print('number of times element occurs in list')
for i in list:
    print('The entry',i, 'is present', list.count(i), 'times')