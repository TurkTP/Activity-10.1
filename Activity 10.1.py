__author__ = 'Luke'
m=[2,4,6,8]
print(m[2])
fivem=[]
for num in m:
    fivem.append(num*5)
    print(fivem)
m.append(10)
print(m)
m.append(6)
print(m)
print(m.index(8))
m.remove(8)
print(m)