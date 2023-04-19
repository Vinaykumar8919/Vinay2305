number = int(input("Enter number:"))
temp =number
rev = 0
rem = 0
while number:
    rem = number%10
    rev = rev*10+rem
    number = number//10
if temp==rev:
    print("Given number is Palindrome")
else:
    print("Given number is not Palindrome")