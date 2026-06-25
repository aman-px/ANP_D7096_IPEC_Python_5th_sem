''' To calculate the perimeter and area of a rectangle. '''
#input the length of the rectangle
length = float(input("Enter the length of the rectangle: "))
#validating the length 
if length <0:
    exit("Length cannot be negative.")
#input the breadth of the rectangle
breadth = float(input("Enter the breadth of the rectangle: "))  
#validating the breadth
if breadth < 0:
    exit("Breadth cannot be negative.")
#-----------------------------------------------------
#displaying data
print("Length of the rectangle: ", length)
print("Breadth of the rectangle: ", breadth)
#-----------------------------------------------------
#displaying perimeter of the rectangle
print("Perimeter of the rectangle: ", 2 * (length + breadth))
#displaying area of the rectangle
print("Area of the rectangle: ", length * breadth)  

''''output:
Enter the length of the rectangle: 5
Enter the breadth of the rectangle: 3
Length of the rectangle:  5.0
Breadth of the rectangle:  3.0
Perimeter of the rectangle:  16.0
Area of the rectangle:  15.0'''