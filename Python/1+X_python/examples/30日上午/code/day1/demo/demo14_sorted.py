

l = [5, 3, 0, -1, 2, 4]
r1 = sorted(l)
print(r1)
r2 = sorted(l, reverse=True)
print(r2)
# key参数表示排序的依据
r3 = sorted(l, key=abs)
print(r3)

