import math

Rx = 0
Ry = 0

forces = 0


forces = input("Number of forces: ")

for i in range(int(forces)):
    force = input("Force: ")
    angle = input("Angle: ")
    a =  math.radians(float(angle))
    Rx += float(force) * math.cos(float(a))
    Ry += float(force) * math.sin(float(a))

print("Resultant: ")
print(math.sqrt(Rx*Rx + Ry*Ry))

print("Angle: ")
print(math.atan(Ry / Rx))