

# taking input from user for calculating distance of a point from origin
x = int(input("Enter the x-coordinate of a point :"))
y = int(input("Enter the y-coordinate of a point :"))

distance = (x*x + y*y)**(1/2)
print("the eucliean distance of a point(", x, ",", y, ") from origin( 0,0 ) : ", distance)

