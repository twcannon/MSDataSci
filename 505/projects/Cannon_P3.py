import csv
import matplotlib.pyplot as plt
import numpy as np

ids = []
with open('./505/data/project_three/ids.txt') as id_file:
    for line in id_file:
        line = line.replace('.txt\n','')
        ids.append(line)

iqs = []
matrices = []
vectors = []
data_dict = {}
i = 0
for id in ids:
    data_dict[id] = {}
    with open('./505/data/project_three/dataset/{}.txt'.format(id)) as iq_file:
        iq = float(iq_file.readline().replace('\n',''))
        iqs.append(iq)
        data_dict[id]['iq'] = iq
    
    matrix = np.genfromtxt('./505/data/project_three/dataset/{}.csv'.format(id),delimiter=',') 
    vector = np.genfromtxt('./505/data/project_three/dataset/{}_vec.csv'.format(id),delimiter=',')
    matrices.append(matrix)
    vectors.append(vector)

    data_dict[id]['pid'] = i
    data_dict[id]['matrix'] = matrix
    data_dict[id]['vector'] = vector

    i += 1

matrices = np.array(matrices)
vectors = np.array(vectors)
regions = list(csv.reader(open("./505/data/project_three/Atlas_regions.csv")))

# # iqs are not normally distributed??
# plt.hist(iqs,bins=20)
# plt.show()



def graphdata(patientid):
    iq=data_dict[patientid]['iq']
    plt.figure(figsize = [10,10])
    plt.imshow(data_dict[patientid]['matrix'])
    plt.set_cmap('hot')
    plt.colorbar()
    plt.title( f"IQ Score of {iq} ")
    plt.show()


graphdata('NS061')