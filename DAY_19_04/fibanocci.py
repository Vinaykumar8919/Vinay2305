n = int(input("Enterp n value: "))
if n<2:
    print("Enter correct number")
else:
    print(0,1,end=" ")
    a,b,c=0,1,1
    for i in range(1,n-2):
        a=b
        b=c
        print(c,end=" ")
        c=a+b
        