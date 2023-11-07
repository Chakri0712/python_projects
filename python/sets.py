s1={1,2,3,4,"name"}
s2={1,"name",3,4}
print(s1.intersection_update(s2))
print(s1)

s1.add(5)
s1.discard("name")
s1.update(s2)
print(s1)
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))