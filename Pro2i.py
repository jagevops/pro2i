def sumpairs(arr):
x = 2
arr = [0 for range(x)]
arr[0] = 1
arr[1] = 2
p = []
getallpairs(arr, 0, x-1,p)

for it in p:
    print(it[0], it(1))
     
