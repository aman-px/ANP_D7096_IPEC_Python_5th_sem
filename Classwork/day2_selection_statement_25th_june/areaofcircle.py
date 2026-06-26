''' To calculate the area and perimeter of a circle. '''
#input of radius.
radius = float(input("Enter the radius of the circle: "))
#validating the radius
if radius < 0:
    exit("Radius cannot be negative. please input a valid input ")
#-----------------------------------------------------
#displaying data to the user
print("Radius of the circle: ", radius)
#-----------------------------------------------------
#displaying area of the circle
print("Area of the circle: ", 3.14 * (radius * radius))
# displaying the perimeter
print("Perimeter of the circle:",2*3.14*radius)