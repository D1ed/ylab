point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)

all_points = [point_1,point_2,point_3,point_4,point_5]

towns = [[],[],[],[],[]]
for c in range(5):
    for i in range(len(all_points)):
        towns[c].append(((all_points[c][0] - all_points[i][0]) ** 2 + (all_points[c][1] - all_points[i][1]) ** 2) ** 0.5)

path =[]
counter = 0
minPath = 10000
minCounter = 0
i1 = 0

for i2 in range(5):
    for i3 in range(5):
        for i4 in range(5):
            for i5 in range(5):
                if i1 != i2 and i1 != i3 and i1 != i4 and i1 != i5 and i2 != i3 and i2 != i4 and i2 != i5 and i3 != i4 and i3 != i5 and i4 != i5:
                    path.append(str(all_points[i1]) + ' → ' + str(all_points[i2])+ '[' + str(towns[i1][i2]) + '] → ' + str(all_points[i3])+ '[' + str(towns[i2][i3]) + '] → ' + str(all_points[i4])+ '[' + str(towns[i3][i4]) + '] → ' + str(all_points[i5])+ '[' + str(towns[i4][i5]) + '] → ' + str(all_points[i1])+ '[' + str(towns[i5][i1])+ '] = ')
                    if (towns[i1][i2] + towns[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i1]) < minPath:
                        minPath = towns[i1][i2] + towns[i2][i3] + towns[i3][i4] + towns[i4][i5] + towns[i5][i1]
                        minCounter = counter
                    counter +=1

result = path[minCounter]+str(minPath)
print(result)