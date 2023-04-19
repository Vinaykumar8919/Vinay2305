num1 = int(input())
num2 = int(input())
num3 = int(input())
min=max=num1
if min>num2:
    min=num2
if min>num3:
    min=num3
if max<num2:
    max=num2
if max<num3:
    max=num3
print(min,num3+num1+num2-max-min,max)