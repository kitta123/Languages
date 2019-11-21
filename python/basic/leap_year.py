year = int(input("Enter the year :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Entered year is leap year")
        else:
            print("Entered year is Not a leap year")
    else:
        print("Entered year is leap year")
else:
    print("Entered year is not leap year")
