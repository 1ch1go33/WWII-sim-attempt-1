#from array import *

list = [[1, 2, 3], [1, 2, 3]]
list.append([2, 3, 4])
list.remove([1, 2, 3])
print(list)
def Hello(x, y, w, h):
    x = 10
    y = 5
    w = 10
    h = 5
    return [x, y, w, h]
list.append(Hello(10, 5, 10, 5))
print(list)