k = input().split()
x1 = int(k[0])

v1 = int(k[1])

x2 = int(k[2])

v2 = int(k[3])


if v2 > v1 and x2 > x1:
    print("NO")
elif x1 > x2 and v1>v2:
    print("NO")
elif x1 != x2 and v1 == v2:
    print("NO")
elif (x1-x2)%(v2-v1) == 0:
    print("YES")
else:
    print("NO")
