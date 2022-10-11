A= { 1,2,3,4,5,6,7}
B = {6,7,8,9}
print(A & B)
print(A.intersection(B)) #INTERSECTION : COMMON IN BOTH

A= { 1,2,3,4,5,6,7}
B = {6,7,8,9}
A - B
print(A.difference(B)) #DIFFERENCE : ELEMENTS ONLY IN A NOT IN B

print(B.difference(A)) # ONLY IN B NOT IN A

#symmetric difference of sets
A= { 1,2,3,4,5,6,7}
B = {6,7,8,9}
A ^ B
print(A.symmetric_difference(B))

