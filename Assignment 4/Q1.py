"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""
Marks=float(input('Enter your marks: '))
if(Marks>=80):
  print('Your grade is A')
elif(80>Marks>=60):
  print('Your grade is B')
elif(60>Marks>=50):
  print('Your grade is C')
elif(50>Marks>=45):
  print('Your grade is D')
elif(45>Marks>=25):
  print('Your grade is E')
else:
  print('Your grade is F')
