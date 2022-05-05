#Taking inputs
a=int(input("Enter a:"))
b=int(input("Enter a:"))
#using the XOR gate such that the 1's in the bit will be the number of bitswitches required
c=a^b
count=0
#counting the number of 1s in c
while(c!=0):
    count=count+1
    c=c&(c-1)
print(count)
