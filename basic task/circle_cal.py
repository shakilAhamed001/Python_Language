radius = float(input("Enter the radius of the circle: "))
pi = 3.14159

# TODO: Calculate diameter, circumference, area
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2

print(f'Radius: {radius}')
print(f'Diameter: {diameter}')
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')