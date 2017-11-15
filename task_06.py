import math
from sys import maxsize
import random


def tsp(data):
    min_length = maxsize
    min_path = list()
    for i in range(len(data)):
        index = i
        data_copy = dc(data)
        length = 0
        path = [index]
        while 1:
            if len(path) == len(data):
                break
            current = data_copy[index]
            data_copy[index] = None
            distances = list()
            for item in data_copy:
                if item is not None:
                    distances.append(find_distance(current, item))
                else:
                    distances.append(None)
            index = find_min_index(distances)
            path.append(index)
            length += distances[index]
        length += find_distance(data[i], data[path[-1]])
        path.append(i)
        if length < min_length:
            min_length = length
            min_path = path
    return min_length, min_path


def find_distance(v1, v2):
    x1, x2, y1, y2 = v1[0], v2[0], v1[1], v2[1]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def find_min_index(li):
    m = maxsize
    ini = 0
    for i in range(len(li)):
        if li[i] is not None and li[i] < m:
            m = li[i]
            ini = i
    return ini


def dc(li):
    new_li = list()
    for i in li:
        new_li.append(i)
    return new_li


def description():
    return """
        1.  assign current (data[0] if not specified)
        2.  length := 0
        3.  path = empty list
        4.  path[0] = current
        5.  find path from current vertex to closest one
        6.  length += found path
        7.  current := closest vertex
        8.  append current to path
        9.  repeat 1. for all vertices in data
        10. print minimum length and its path
    """


def verify(data, index_list):
    length = 0
    for i in range(len(index_list[:-1])):
        length += find_distance(data[index_list[i]], data[index_list[i + 1]])
    return length


# x = True
# li = list()
# while x:
#     x = input()
#     li.append([int(i) for i in x.split()])
# li = li[:-1]
# print(tsp(li))

# x = [[1, random.randrange(100)] for i in range(100)]
x = [[1380, 939], [2848, 96], [3510, 1671], [457, 334], [3888, 666], [984, 965], [2721, 1482], [1286, 525],
     [2716, 1432], [738, 1325], [1251, 1832], [2728, 1698], [3815, 169], [3683, 1533], [1247, 1945], [123, 862],
     [1234, 1946], [252, 1240], [611, 673], [2576, 1676], [928, 1700], [53, 857], [1807, 1711], [274, 1420],
     [2574, 946], [178, 24], [2678, 1825], [1795, 962], [3384, 1498], [3520, 1079], [1256, 61], [1424, 1728],
     [3913, 192], [3085, 1528], [2573, 1969], [463, 1670], [3875, 598], [298, 1513], [3479, 821], [2542, 236],
     [3955, 1743], [1323, 280], [3447, 1830], [2936, 337], [1621, 1830], [3373, 1646], [1393, 1368], [3874, 1318],
     [938, 955], [3022, 474], [2482, 1183], [3854, 923], [376, 825], [2519, 135], [2945, 1622], [953, 268],
     [2628, 1479], [2097, 981], [890, 1846], [2139, 1806], [2421, 1007], [2290, 1810], [1115, 1052], [2588, 302],
     [327, 265], [241, 341], [1917, 687], [2991, 792], [2573, 599], [19, 674], [3911, 1673], [872, 1559], [2863, 558],
     [929, 1766], [839, 620], [3893, 102], [2178, 1619], [3822, 899], [378, 1048], [1178, 100], [2599, 901],
     [3416, 143], [2961, 1605], [611, 1384], [3113, 885], [2597, 1830], [2586, 1286], [161, 906], [1429, 134],
     [742, 1025], [1625, 1651], [1187, 706], [1787, 1009], [22, 987], [3640, 43], [3756, 882], [776, 392], [1724, 1642],
     [198, 1810], [3950, 1558]]
a = tsp(x)
print(a)
print(verify(x, a[1]))
print(description())
