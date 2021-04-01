import numpy as np
n, m = [int(x) for x in input().split()]
arr=[]
for i in range(n):
    arr.append([int(x) for x in input().split()])
print(np.array(arr).transpose())
print(np.array(arr).flatten())
