def binToDec(bin):
    decimal = 0
    count = 0
    while(bin != 0):
        digit = bin % 10
        decimal = decimal + digit * pow(2, count)
        bin = bin//10
        count += 1
    return decimal

if __name__ == '__main__':
    binary = int(input("Enter a binary value: "))
    print("decimal of binary ", binary, " is: ", binToDec(binary))
