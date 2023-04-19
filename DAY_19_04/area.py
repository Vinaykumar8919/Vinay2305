print("1.traingle 2.rectangle 4.square")
choice = int(input("Enter you choice: "))
if choice==1:
    base = float(input("Enter base: "))
    height=float(input("Enter height: "))
    print("Area of traingle is ", 0.*base*height)
elif choice==2:
    base = float(input("Enter length: "))
    height=float(input("Enter breadth: "))
    print("Area of rectangle is ", base*height)
elif choice==3:
    side = float(input("Enter value of side : "))
    print("are of square  is", side*side)
else:
    print("Invalid choice")