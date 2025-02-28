#Day 3
age = 18                #1
height = 1.78           #2
complex_var = 2+3j      #3

base_triangle = float(input("Enter the base of a triangle: "))          #4
height_triangle = float(input("Enter the height of a triangle: "))
area_triangle = (base_triangle * height_triangle)/2
print("The area of the triangle is ", area_triangle)

side_a = float(input("Enter side A: "))                                 #5
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)

length = float(input("Insert the length of a rectangle: "))             #6
width = float(input("Insert the width of a rectangle: "))
area_rectangle = length*width
print(area_rectangle)

r = float(input("Enter the value of the radius: "))                     #7
area_of_circle = (r**2)*3.14
circum_of_circle = 2*r*3.14
print("The area of your circle is", area_of_circle)
print("The circumference of your circle is: ", circum_of_circle)

slope = 2                                                               #8
y_inter = -2
x_inter = (slope*0 - y_inter)/slope
print("The slope of the ecuation is: ", int(slope))
print("The x-intercept of the ecuation is: ", int(x_inter))
print("The y-intercept of the ecuation is: ", int(y_inter))

x1, x2, y1, y2 = 2, 6, 2, 10                                            #9
slope_2 = (y2 - y1)/(x2 - x1)
euclidean_dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print("The distance between the points is: ", euclidean_dist)
print("The slope of the second ecuation is: ", int(slope_2))

print("Are the two slopes equal? ", slope == slope_2)                   #10


for x in range(-10, 11):                                                #11
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y is equal to 0 when x has a value of: {x}")

