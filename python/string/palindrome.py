'''' function which return reverse of a string '''

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False

s = input("Enter the string :")
ans = isPalindrome(s)
if ans == 1:
    print("Yes")
else:
    print("No")



string=input(("Enter a string:"))
if(string==string[::-1]):
      print(string,"The string is a palindrome")
else:
      print(string,"Not a palindrome")
