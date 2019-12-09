def rotate(a,d):

    Lfirst = a[0 : d]
    Lsecond = a[d :]
    Rfirst = a[0 : len(a)-d]
    Rsecond = a[len(a)-d : ]

    print("Left Rotated String : ", (Lsecond + Lfirst))
    print("Right Rotated String : ", (Rsecond + Rfirst))


str = input("Enter the string :")
digit = int(input("Enter the digit :"))
rotate(str,digit)
