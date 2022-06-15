no_of_rows = int(input('enter the number of rows you want to see: '))

k = 65
for i in range(1, no_of_rows+1):
    for j in range(i):
        y = chr(k)
        print(y, end="")
        k += 1
        if (k-64)%26 == 0:
            k = 65
    print("")

print("\n")
    