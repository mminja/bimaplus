# BIM A+ 3 - Parametric Modelling in BIM
# Topic 2: Fundamentals of programming
# Programming assignment 03
# Python program to calculate geometrical characteristics for any polygon

# Minja Radenkovic

print("The Python program calculates different geometrical characteristics for a polygon\n")
print()


# Ask the user how many points are there for the polygon
n = int(input("Enter the number of polygon points: \n"))
print()


# Create the coordinates list
x = []
y = []
print()


# Ask the user to input the coordinates, starting x and y for the first point, then for the second, so forth
print("Enter x and y coordinates for polygon points: ")
for i in range(n):
    x.append(float(input("enter x coordinate of point " + str(i) + ": " )))
    y.append(float(input("enter y coordinate of point " + str(i) + ": " )))
print()


# Print table of points
print("Pt" + f"{'x':>10} {'y':>10}")
print("-" * 30)  
for i in range(n):
    print(i+1, ":",     f"{x[i]:>7} {y[i]:>10}")
print()


# Calculations

Ax = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0

for i in range (n):
    xi1 = x[i]
    xi = x[i-1]
    yi1 = y[i]
    yi = y[i-1]

    Ax = Ax + (xi1 + xi) * (yi1 - yi)
    
    Sx = Sx + (xi1 - xi) * (yi1**2 + yi * yi1 + yi**2 )
    Sy = Sy + (yi1 - yi) * (xi1**2 + xi * xi1 + xi**2 )

    Ix = Ix + (xi1 - xi) * ( yi1**3 + yi1**2 * yi + yi1 * yi**2 + yi**3)
    Iy = Iy + (yi1 - yi) * ( xi1**3 + xi1**2 * xi + xi1 * xi**2 + xi**3)
    Ixy = Ixy + (yi1 - yi) * (yi1 * (3 * xi1**2 + 2 * xi1 * xi + xi**2) + yi * (3 * xi**2 + 2 * xi * xi1 + xi1**2))

Ax = Ax / 2
Sx = Sx / (-6)
Sy = Sy / 6
Ix = Ix / (-12)
Iy = Iy / 12
Ixy = Ixy / (-24)

xt = Sy / Ax
yt = Sx / Ax
Ixt = Ix - yt**2 * Ax
Iyt = Iy - xt**2 * Ax
Ixyt = Ixy + xt * yt * Ax

#Print all final results of geometrical characteristics
print("Geometric Characteristics")
print()

print(f"Ax = {Ax:.2f}")
print(f"Sx = {Sx:.2f}")
print(f"Sy = {Sy:.2f}")
print(f"Ix = {Ix:.2f}")
print(f"Iy = {Iy:.2f}")
print(f"Ixy = {Ixy:.2f}")
print(f"xt = {xt:.2f}")
print(f"yt = {yt:.2f}")
print(f"Ixt = {Ixt:.2f}")
print(f"Iyt = {Iyt:.2f}")
print(f"Ixyt = {Ixyt:.2f}")
print()

print("End")