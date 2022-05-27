from random import randint as numf
var=1
n=1
while(var==1):
  
  x=numf(0,20)
  y=numf(0,20)
  print('Question',n,'what is ',x,'*',y,'=')
  ans=int(input())
  n=n+1
  if(ans == x*y):
    print('Right!')
  else:
    print('Wrong.The answer is',x*y)