import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.decomposition import PCA 
from sklearn.feature_selection import VarianceThreshold,SelectFromModel
from sklearn.linear_model import LogisticRegression,SGDClassifier,Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, confusion_matrix
from sklearn.model_selection import StratifiedKFold,KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.svm import SVC



import sys



ids = []
with open('./505/data/project_three/ids.txt') as id_file:
    for line in id_file:
        line = line.replace('.txt\n','')
        ids.append(line)

iqs = []
iqs_labels = []
matrices = []
vectors = []
data_dict = {}
i = 0
for id in ids:
    data_dict[id] = {}
    with open('./505/data/project_three/dataset/{}.txt'.format(id)) as iq_file:
        iq = float(iq_file.readline().replace('\n',''))
        iqs.append(np.array([iq]))
        iqs_labels.append([iq,int(0 if iq<100 else 1),str('above average' if iq>110 else ('below average' if iq<90 else 'average'))])
        data_dict[id]['iq'] = [iq,int(0 if iq<100 else 1),str('above average' if iq>110 else ('below average' if iq<90 else 'average'))]
    
    matrix = np.genfromtxt('./505/data/project_three/dataset/{}.csv'.format(id),delimiter=',') 
    vector = np.array([np.array(np.genfromtxt('./505/data/project_three/dataset/{}_vec.csv'.format(id),delimiter=','))])
    # print(vector)
    # print(np.array([vector]))
    # print(np.shape(vector[0]))
    # print(np.shape(np.array([vector])))
    matrices.append(matrix)
    vectors.append(vector[0])

    data_dict[id]['pid'] = i
    data_dict[id]['matrix'] = matrix
    data_dict[id]['vector'] = vector

    i += 1

# iqs[np.newaxis,:]

matrices = np.array(matrices)
vectors = np.array(vectors)
iqs = np.array(iqs)
regions = list(csv.reader(open("./505/data/project_three/Atlas_regions.csv")))

# print(np.shape(vectors[0]))
# print(vectors[:,0])
# print(np.shape(vectors[:,0]))

# print(np.shape(vectors))
# print(np.shape(iqs))



# pca = PCA(.8)
# pca.fit(vectors_train)
# new_columns = pca.fit_transform(vectors_train)
# print(pca.__dict__)
# print(np.shape(vectors_train))
# print(np.shape(vectors_train[:,0:50]))
# print(np.shape(new_columns))



pca = PCA(.8)
pca.fit(vectors)
vectors = pca.fit_transform(vectors)
print(pca.__dict__)
print(np.shape(vectors))
# print(np.shape(vectors[:,0:50]))
# print(np.shape(new_columns))



skf = KFold(n_splits=10,shuffle=True)
# skf.get_n_splits(vectors, iqs)

print(vectors)
print(iqs)
print(np.shape(vectors))
print(np.shape(iqs))
# print(skf.split(vectors,iqs))
for train_index, test_index in skf.split(vectors,iqs):
    print("TRAIN:", train_index, "TEST:", test_index)
    vectors_train, vectors_test = vectors[train_index], vectors[test_index]
    iqs_train, iqs_test = iqs[train_index], iqs[test_index]



# plt.hist(vectors[:,0],bins=10)
# plt.hist(new_columns[8],bins=10)
# plt.show()

# plt.boxplot(vectors[:,0:50])

# plt.boxplot(vectors[:,51:100])
# plt.show()

linreg = linear_model.LinearRegression()
linreg.fit(vectors_train,iqs_train)
print(linreg.__dict__)
# use the model fit to build a prediction from the test data
Yhat = linreg.predict(vectors_test)
print(linreg.__dict__)
# print('r coefficients: \n\tX1 '+str(linreg.coef_[0])+'\n\tX2 '+str(linreg.coef_[1]))


MSE = mean_squared_error(iqs_test, Yhat)
RMSD = np.sqrt(mean_squared_error(iqs_test, Yhat))
MAE = mean_absolute_error(iqs_test, Yhat)
print('MSE: {0:0.3f}'.format(MSE))
print('RMSD: {0:0.3f}'.format(RMSD))
print('MAE: {0:0.3f}'.format(MAE))

sys.exit()






sys.exit('')


def graphdata(patientid):
    iq=data_dict[patientid]['iq']
    plt.figure(figsize = [10,10])
    plt.imshow(data_dict[patientid]['matrix'])
    plt.set_cmap('hot')
    plt.colorbar()
    plt.title( f"IQ Score of {iq} ")
    plt.show()


graphdata('NS061')






pipe_steps = [  ('feature_engineering', [
                    ('VT', VarianceThreshold()),
                    ('PCA', PCA())]),
                ('scaler', [
                    ('standard', StandardScaler()),
                    ('minmax', MinMaxScaler())]),
                ('classifier', [
                    ('LR', LogisticRegression()),
                    ('SVC', SVC()),
                    ('SGD', SGDClassifier())])]

# Grid search parameters for our models
param_grid = {'LR': {'penalty': ['l1', 'l2']},
              'SVC': {'kernel': ['linear', 'poly', 'rbf', 'sigmoid']},
              'SGD': {'penalty': ['elasticnet'],
                      'l1_ratio': [0.1, 0.2, 0.3]}}

# Quality metric that we want to optimize
scoring='roc_auc'

# Setting cross-validations
grid_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
eval_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

# >>> anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])
# >>> # You can set the parameters using the names issued
# >>> # For instance, fit using a k of 10 in the SelectKBest
# >>> # and a parameter 'C' of the svm
# >>> anova_svm.set_params(anova__k=10, svc__C=.1).fit(X, y)