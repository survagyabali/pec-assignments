import math as m
# a
print((3+4)*5)
# b
n=int(input())
exp=n*(n-1)/2
print(exp)
# c 
r=float(input())
exp =4* m.pi*r**2
print(exp)
# d
#Taking inputs of a,b and r 
a=float(input('Enter value of a:'))
b=float(input('Enter value of b:'))
r=float(input('Enter value of r:'))
#Expression 
exp=(r*(m.cos(a))**2 + r*(m.sin(b))**2)**0.5
#printing the resultant 
print('the result from the expression is:',exp)
#e
#taking inputs
x1=float(input('Enter value of x1:'))
x2=float(input('Enter value of x2:'))
y1=float(input('Enter value of y1:'))
y2=float(input('Enter value of y2:'))
#plugging inputs in the expresstion
exp=(y2-y1)/(x2-x1)
#printing expression
print('The resulting value of this expression will be:',exp)
