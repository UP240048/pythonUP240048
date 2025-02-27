#Day 3
age = 18
height = 1.78
complex_var = 2+3j

base_triangle = float(input("Enter the base of a triangle: "))
height_triangle = float(input("Enter the height of a triangle: "))
area_triangle = (base_triangle * height_triangle)/2
print("The area of the triangle is ", area_triangle)

side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)

length = float(input("Insert the length of a rectangle: "))
width = float(input("Insert the width of a rectangle: "))
area_rectangle = length*width
print(area_rectangle)

r = float(input("Enter the value of the radius: "))
area_of_circle = (r**2)*3.14
circum_of_circle = 2*r*3.14
print("The area of your circle is", area_of_circle)
print("The circumference of your circle is: ", circum_of_circle)

