#Day 2: 30 Days of python programming
#Level 1
first_name, last_name, age = "David", "Padilla", 18
full_name = first_name + " " + last_name
country, city, year = "México", "Aguascalientes", 2025
is_married, is_true, is_light_on = False, False, True

#Level 2
print(type(first_name), type(last_name), type(age))
print(type(full_name))
print(type(country), type(city), type(year))
print(type(is_married), type(is_true), type(is_light_on))

print("Length of first and last names: ", len(first_name), "and", len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

r=30
area_of_circle = (r**2)*3.14159
circum_of_circle = 2*r

input_radius = float(input("Enter the value of the radius: "))
area_user = (input_radius**2)*3.14159
print ("The area of your circle is", area_user)

first_name, last_name, country, age = input("Please enter your first and last names, your country and your age, separated by a coma and a space: ").split(", ")
print(first_name, last_name, country, age)

help("keywords")