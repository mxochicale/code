import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from math import sqrt

from numpy import loadtxt

from xgboost import XGBClassifier
#from lightgbm import LGBMClassifier

from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, accuracy_score, r2_score, f1_score, classification_report

## using local dataset  #X(768, 8); Y(768,)
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]

### Using breast_cancer  #X(569, 30); Y(569,)
#bc = datasets.load_breast_cancer()
#X = bc.data
#Y = bc.target

## Printing shape of data
print(np.shape(X)) 
print(np.shape(Y)) 

## split data into train and test sets
#seed = 3
#seed = 5
seed = 7 ##Default

#test_size = 0.4
#test_size = 0.3
#test_size = 0.33 ##Default
#test_size = 0.2
#test_size = 0.13
test_size = 0.1
#test_size = 0.05

X_train, X_test, y_train, y_test = \
   train_test_split(X, Y, test_size=test_size, random_state=seed)

#print(np.shape(X_train))  #(514, 8)
#print(np.shape(X_test)) #(254, 8)
#print(np.shape(y_train)) #(514,)
#print(np.shape(y_test)) #(254,)

## fit model no training data
params = {}
##ESTIMATORS
#params['n_estimators'] = 5 #000
#params['n_estimators'] = 50 #000
#params['n_estimators'] = 100 #000
#params['n_estimators'] = 1000 #000
#params['n_estimators'] = 2000 #000
#params['n_estimators'] = 2500 #000
#params['n_estimators'] = 4000 #000
params['n_estimators'] = 5000 #000
#params['n_estimators'] = 10000 #000
##LEARNING RATE
#params['learning_rate'] = 0.1
#params['learning_rate'] = 0.05
#params['learning_rate'] = 0.01
#params['learning_rate'] = 0.005
params['learning_rate'] = 0.001
#params['learning_rate'] = 0.0005
#params['learning_rate'] = 0.0001
#params['learning_rate'] = 0.00001
##SEED
#params['seed'] = 27
#params['max_depth']=2
#params['min_child_weight']=1
#params['gamma']=0
#params['subsample']=0.8
#params['colsample_bytree']=0.8
#params['objective']= 'binary:logistic'
#params['nthread']=4
#params['scale_pos_weight']=1
##BOOSTER
params['booster']='gbtree'
#params['booster']='gblinear'
#params['booster']='dart' #take more time
##DEVICE
params['device']='cpu'
#params['device']='gpu'
#params['device']='cuda'


##MODEL SELECTION
#params_lgbm = {}
#params_lgbm['random_state'] = 47
#model = LGBMClassifier()
#model = LGBMClassifier(**params_lgbm)

#model = XGBClassifier()
model = XGBClassifier(**params)


evalsetlist = [(X_train, y_train), (X_test,y_test)]
#print(type(evalset)) #<class 'list'>


#model.fit(X_train, y_train)
model.fit(X_train, y_train, eval_metric='logloss', eval_set=evalsetlist)

#print(model)

## make predictions for test data
y_pred = model.predict(X_test)
#print(y_pred)
y_preds = [round(value) for value in y_pred]
#print(y_preds)
#print(np.shape(y_preds)) # (254,)
#print(y_preds)
#print(np.shape(y_preds)) # (254,)


## evaluate predictions
#print(y_test)
#print(y_preds)

accuracy = accuracy_score(y_test, y_preds)
score = f1_score(y_test, y_preds)
MSE = mean_squared_error(y_test, y_preds) 
RMSE = sqrt(mean_squared_error(y_test, y_preds)) 
R2score = r2_score(y_test, y_preds)  

print("Accuracy: %.2f%%" % (accuracy * 100.0))
print('F1 score: %.3f' % score)
print('MSE: ', MSE)
print('RMSE: ', RMSE)
print('R2score :', R2score)
print(classification_report(y_test, y_preds))


#### Results
results = model.evals_result()
plt.plot(results['validation_0']['logloss'], label='train')
plt.plot(results['validation_1']['logloss'], label='test')
plt.title("Loss curves")
plt.xlabel("Epochs")
plt.ylabel("Logloss")
plt.grid()
plt.legend()
plt.show()


##totest
#y_test.corr(y_preds)

