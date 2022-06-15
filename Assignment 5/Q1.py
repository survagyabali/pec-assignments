#taking string input
String=input('')
# Reversing string using for loop
n=len(String)
i=0
for i in range(n):
  print(String[n-i-1],sep='',end='')
  