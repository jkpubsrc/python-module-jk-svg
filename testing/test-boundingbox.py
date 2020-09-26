#!/usr/bin/python3




from jk_svg import *







b1 = BoundingBox(1, 1, 3, 3)
b2 = BoundingBox(2, 2, 4, 4)

print(b1.union(b2))
print(b1.intersection(b2))

b1 = BoundingBox(1, 1, 3, 3)
b2 = BoundingBox(2, 2, 4, 4)

print(BoundingBox.uniteMany(b1, b2))
print(BoundingBox.intersectMany(b1, b2))




