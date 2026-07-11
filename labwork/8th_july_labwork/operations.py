from twodfigures import *

print("Choose the 2D figure to perform the operations :")
print("1: Circle")
print("2: Square")
print("3: Rectangle")
print("4: Triangle")
print("5: Exit")

choose = int(input("Enter your choice (1-5): "))

if choose == 1:
    radius = float(input("Enter the radius of the circle: "))
    
elif choose == 2:
    side = float(input("Enter the side of the square: "))
    
elif choose == 3:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    
elif choose == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    
elif choose == 5:
    print("Exiting...")
else:
    print("Invalid choice. Please choose a valid option (1-5).")

operation = int(input("Enter the operation (1 : area, 2 : perimeter): "))

if choose == 1:
    if operation == 1:
        print("Area of the circle:", circle_area(radius))
    elif operation == 2:
        print("Perimeter of the circle:", circle_perimeter(radius))
    else:
        print("Invalid operation. Please choose a valid option (1-2).")
if choose == 2:
    if operation == 1:
        print("Area of the square:", square_area(side))
    elif operation == 2:
        print("Perimeter of the square:", square_perimeter(side))
    else:
        print("Invalid operation. Please choose a valid option (1-2).")
if choose == 3:
    if operation == 1:
        print("Area of the rectangle:", rectangle_area(length, breadth))
    elif operation == 2:
        print("Perimeter of the rectangle:", rectangle_perimeter(length, breadth))
    else:
        print("Invalid operation. Please choose a valid option (1-2).")
if choose == 4:
    if operation == 1:
        print("Area of the triangle:", triangle_area(base, height))
    elif operation == 2:
        print("Perimeter of the triangle:", triangle_perimeter(side1, side2, side3))
    else:
        print("Invalid operation. Please choose a valid option (1-2).")
if choose == 5:
    print("Exiting...")
