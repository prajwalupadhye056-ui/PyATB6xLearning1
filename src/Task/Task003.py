#Write a python program to calculate the area of circle given its radius using the formula

#area =pi*r^2(Take pi as 3.14)

#i/p -r-> float
#o/p -> String formatted output of the area

radius= float(input("Enter the radius \n"))
print(radius)

area = 3.14 *(pow(radius,2))
print("Area of the circle is -> ", area)

#String data formatting Python- f-Strings, formatted string literals
print(f"Area of the circle is -> {area:.2f}")