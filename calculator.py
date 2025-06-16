print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Let's calculate some shapes!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(" ")
print("Choose which area shape to calculate by entering the corresponding number.")

shapes = ["Square", "Rectangle", "Triangle", "Circle"]
for idx, shapelist in enumerate(shapes, 1):
    print(f"{idx}. {shapelist}")
selected = int(input(" "))
print(' ')

if selected == 1: #square area = x**
    sidex = float(input("What is the length or width? "))
    squarearea = sidex*sidex
    print(" ")
    print(f"The area of your square is {squarearea}.")
elif selected == 2: #rectangle area = length * width
    length_rectangle = float(input("What is the length? "))
    width_rectangle = float(input("What is the width? "))
    rectangle_area = length_rectangle*width_rectangle
    print(" ")
    print(f"The area of your rectangle is {rectangle_area}.")
elif selected == 3: #triangle. area = (height*base)/2
    height = float(input("What is the height? "))
    base = float(input("What is the base? "))
    triangle_area = (height*base)/2
    print(" ")
    print(f'The area of your triangle is {triangle_area}.')
elif selected == 4: #cirlce. area = pi * radius^2
    radius = float(input("What is the radius? "))
    circle_area = 3.14*radius**2
    print(" ")
    print(f'The area of your circle is {circle_area}.')
else:
    print("Input not valid, please enter a number from the list that corresponds to a shape.")
print(" ")
