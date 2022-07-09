# number of rows input
n=int(input('Rows'))
#spaceing so it prints in a triangle
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # 1 is always first so its outside for loop
    a = 1
    for j in range(1, i+1):
 
        
        print(' ', a, sep='', end='')
 
        # binomial series
        a = a * (i - j) // j
    print('')