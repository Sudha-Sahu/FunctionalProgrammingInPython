# calculating roots of a quadratic equation

print("enter the coefficient of quadratic equation:")
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

delta = (b*b * 4*a*c)**(1/2)
root1 = (-b + delta)/(2*a)
root2 = (-b - delta)/(2*a)
print("the 2 Roots of quadratic equation are : ", root1, " , ", root2)

