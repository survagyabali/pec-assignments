#Taking integer inputs
year = int(input("Enter year: "))
#Setting conditions with if and elifs
if year % 400 == 0 :
    print(year, "is a Leap Year")
elif year % 100 == 0 :
    print(year, "is not a Leap Year")
elif year % 4 == 0 :
    print(year, "is a Leap Year")
else :
    print(year, "is not a Leap Year")