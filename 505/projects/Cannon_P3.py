import numpy as np
import csv

ids = []
with open('./505/data/project_three/ids.txt') as id_file:
    for line in id_file:
        line = line.replace('.txt\n','')
        ids.append(line)

iqs = []
data = []
for id in ids:
    with open('./505/data/project_three/dataset/{}.txt'.format(id)) as iq_file:
        iqs.append(iq_file.readline().replace('\n',''))
    brain_data = np.genfromtxt('./505/data/project_three/dataset/{}.csv'.format(id),delimiter=',') 
    data.append(brain_data)
# print(iqs)

data = np.array(data)
# print(data)

regions = list(csv.reader(open("./505/data/project_three/Atlas_regions.csv")))
# print(regions)