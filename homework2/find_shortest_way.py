point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)
#point_6 = (20, 16)

all_points = [point_1,point_2,point_3,point_4,point_5]
#all_points = [point_1,point_2,point_3,point_4,point_5,point_6]

from sys import maxsize
from itertools import permutations

towns = [[] for i in range(len(all_points))]


for c in range(len(all_points)):
    for i in range(len(all_points)):
        towns[c].append(((all_points[c][0] - all_points[i][0]) ** 2 + (all_points[c][1] - all_points[i][1]) ** 2) ** 0.5)
 
def tsp(towns):
    vertex = []
    store = []
    store = []
    for i in range(len(all_points)):
        if i != 0:
            vertex.append(i)
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        store.append(i)
        current_pathweight = 0
        k = 0
        for j in i:
            current_pathweight += towns[k][j]
            k = j
        current_pathweight += towns[k][0]
        store.append(current_pathweight)
        min_path = min(min_path, current_pathweight)
    x = 0
    res = ()
    while x != 1:
        for i in range(len(store)):
            if store[i] == min_path:
                res = store[i-1]
                x = 1
    end = str(all_points[0])
    start_point = 0           
    for i in res:
        end += ' → ' + str(all_points[i])+ '[' + str(towns[start_point][i]) + ']'
        start_point = i
    end += ' → ' + str(all_points[0])+ '[' + str(towns[start_point][0]) + '] = ' + str(min_path)
    return print(end)

tsp(towns)