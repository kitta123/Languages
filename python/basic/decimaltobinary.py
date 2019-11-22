# def DecimalToBinary(num):
#     if num > 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
#
# if __name__ == '__main__':
#     decimal = int(input("Enter a decimal number to convert to binary :"))
#     DecimalToBinary(decimal)

# n=int(input("Enter a number: "))
# a=[]
# while(n>0):
#     dig=n%2
#     a.append(dig)
#     n=n//2
# a.reverse()
# print("Binary Equivalent is: ")
# for i in a:
#     print(i,end=" ")

#Using Recursion:
def decToBin(n):
    if(n == 0):
        return "0"
    bin = "";
    while (n > 0):
        if (n & 1 == 0):
            bin = '0' + bin
        else:
            bin = '1' + bin
        n = n >> 1
    return bin

n = int(input("Enter the number to convert to binary :"))
print(decToBin(n))
