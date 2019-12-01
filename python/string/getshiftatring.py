def rotate(input,d):

    Lfirst = input[0 : d]
    Lsecond = input[d :]
    Rfirst = input[0 : len(input)-d]
    Rsecond = input[len(input)-d : ]

    print("Left Rotated String : ", (Lsecond + Lfirst))
    print("Right Rotated String : ", (Rsecond + Rfirst))


str = input("Enter the string :")
digit = int(input("Enter the digit :"))
rotate(str,digit)
