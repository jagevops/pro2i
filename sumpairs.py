x = [0, 1, 2, 3, 4, 5]
print ("The original list is : " + str(x))
res = []
for i in range(len(x)):
    res.append((x[i], x[(i + 1) % len(x)]))
print("The pair list is :", res)