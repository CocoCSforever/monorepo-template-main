s = [10, 20, 30, 40, 30, 50]
x = 30

print(s[-7])

# Find the index of 30 in the list, starting from index 2

# index = s.index(x, 2, 2)
# print(index) # ValueError: 30 is not in list

index = s.index(x, 2, 3)
print(index) # 2

a = [[2, 3] * 2] * 2
print(a)
a[0][0] = 5
print(a)
# [[2, 3, 2, 3], [2, 3, 2, 3]]
# [[5, 3, 2, 3], [5, 3, 2, 3]]

# shallow copy
c = [10, [10, 20], 20]
c1 = c[:2]
print(c1)
c1[1][0] = 20
print(c)

c2 = list(c)
c2[1][0] = 10
print(c)


dict = {"a": 1, "b": 2}
values = dict.values()
values2 = dict.values()
print(values)
print(values2)
print(type(values))
print(type(values2))
print(values == values2)
print(dict.values() == dict.values())
print(values == values)
