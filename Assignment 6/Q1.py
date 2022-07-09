n = int(input('Enter'))
l = []


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            l.append(i)

    print(l)


isprime(n)
sum = 1
for i in l:
    sum = i + sum
    print(sum)
if sum == n:
    print('Perfect Number')
else:
  print('False')
