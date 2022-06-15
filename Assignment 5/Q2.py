#Taking input for range limits
R_start=int(input('Range Start:'))
R_end=int(input('Range End:'))

int=int(input('Integer:'))
#checking divisibility using for loop
for i in range(R_start,R_end):
  if(i%int==0):
    print(i)