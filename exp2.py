import math

Rx = 0
Ry = 0

Ax = 0
Ax = 0

# sup1 = input("Enter type of support 1").lower()
# sup2 = input("Enter type of support 2").lower()

forces = 0

forces = input("Enter number of forces")

for i in range(int(forces)): 
    force = input("Force: ")
    angle = input("Angle: ")
    a =  math.radians(float(angle))
    Rx += float(force) * math.cos(float(a))
    Ry += float(force) * math.sin(float(a))

print("Resultant: ")
print(math.sqrt(Rx*Rx + Ry*Ry))

a = input("Input forces about A: ")
sumA = 0
B = 0
for i in range(int(a)):
    force = input("Force: ")
    angle = input("Angle: ")
    distance = input("Distance: ")
    sumA += force * math.sin(float(math.radians(angle))) * distance

length = input("Length: ")
B = -sumA/length
A = Ry - B

print("vertical reaction at A: ")
print(A)

print("vertical reaction at B: ")
print(B)

