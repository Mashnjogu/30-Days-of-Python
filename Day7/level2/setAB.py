A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#join A and B
C = A.union(B)
print(C)
#Find A intersection B
print(A.intersection(B))
#Is A a subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
AB = A.union(B)
BA = B.union(A)
CAB = AB.union(BA)
print(CAB)
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
del A
del B



BA = B.update(A)

