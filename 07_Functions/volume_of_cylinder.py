def volume_cylinder(radius, height):
    volume = 3.14 * radius * radius * height
    return volume

rad = float(input("Enter the value of radius: "))
height = float(input("Enter the value of height: "))
print("Volume of Cylinder is ", volume_cylinder(radius = rad, height = height))