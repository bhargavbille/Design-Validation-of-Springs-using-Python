import math
from math import ceil
md = float(input("3. Designing of Torsional Springs\n\tEnter the mean diameter : "))
tm = float(input("\tEnter the Torsional moment applied in Nm : "))
s = float(input("\tEnter the Spring Index : "))
ps = float(input("\tEnter the Permissible Stress in the Spring in N/mm2 : "))
e = float(input("\tEnter the Modulus of Elasticity in N/mm2 : "))
c = float(input("\tEnter the no. of Effective Coils : "))
d = ceil(((32*tm*1.08*(10**3))/(ps*math.pi)) ** (1/3))
if d%2 == 0 or d%5 == 0:
    d = d
else:
    d += 1
t = round((64*tm*(10**3)*md*c)/(e*(d**5)),3)
tt = 180/math.pi * t
print("Result :...................................\n\tThe Diameter of the Wire (d) = %.2f" %d)
print("\tDeflection in radians = %.3f\n\tDeflection in Degrees = %.3f" %(t,tt))
