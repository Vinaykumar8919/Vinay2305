number = input("Enter number : ")
n = len(number)
temp=number=int(number)
sum = 0
rev =0
while number:
    rev = number%10
    sum = sum + pow(rev,n)
    number = number//10
if temp==sum:
    print("Given Number is AramStrong Number")
else:
    print("Given Number is Not AramStrong Number")