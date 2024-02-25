from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import mean_squared_error, accuracy_score, r2_score, f1_score, classification_report

from sklearn.datasets import make_classification

import time
from tqdm import tqdm
from math import sqrt

## NOTES 
#from tqdm.notebook import tqdm #cause i`AttributeError: 'tqdm_notebook' object has no attribute 'disp'` FROM https://stackoverflow.com/questions/56794127


# configuration for our custom dataset
min_samples = 1000
max_samples = 20000
step = 1000


##Setting parameters
params_xgb = {}
params_xgb['n_estimators'] = 100 #1000
params_xgb['seed'] = 47

params_lgbm = {}
params_lgbm['random_state'] = 47


for sample_size in tqdm(range(int(min_samples/0.8), int(max_samples/0.8),step)):
    #print(f"\n sample_size: {sample_size}")
    xgb_dummy = XGBClassifier(**params_xgb)
    lgbm_dummy = LGBMClassifier(**params_lgbm)

    # logging the sample size
    #run['metrics/comparison/sample_size'].log(sample_size)

    # Generating the dataset of custom sample size
    dummy = make_classification(n_samples=sample_size)
    #print(dummy[0].shape)
    #print(dummy[1].shape)

    # Splitting the data into train and test set
    X_train, X_test, y_train, y_test = train_test_split(
                                                     dummy[0],
                                                     dummy[1],
                                                     test_size=0.2,
                                                     stratify=dummy[1]
                                                     )


    evalset = [(X_train, y_train), (X_test,y_test)]
 
    start = time.time()
    #xgb_dummy.fit(X_train, y_train)
    xgb_dummy.fit(X_train, y_train, eval_metric='logloss', eval_set=evalset)
    end = time.time()

    predictions = xgb_dummy.predict(X_test)
    results = xgb_dummy.evals_result()
    #print(results)


    accuracy = accuracy_score(y_test, predictions)
    score = f1_score(y_test, predictions)
    MSE = mean_squared_error(y_test, predictions) 
    RMSE = sqrt(mean_squared_error(y_test, predictions)) 
    R2score = r2_score(y_test, predictions)  


    print(f"####################################################")
    print(f"### xgb_dummy; execution time:{end-start}")

    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print('F1 score: %.3f' % score)
    print('MSE: ', MSE)
    print('RMSE: ', RMSE)
    print('R2score :', R2score)
    print(classification_report(y_test, predictions))

    start = time.time()
    lgbm_dummy.fit(X_train, y_train)
    ypredl = lgbm_dummy.predict(X_test)

    accuracy = accuracy_score(y_test, ypredl)
    score = f1_score(y_test, ypredl)
    MSE = mean_squared_error(y_test, ypredl) 
    RMSE = sqrt(mean_squared_error(y_test, ypredl)) 
    R2score = r2_score(y_test, ypredl)  

    end = time.time()
    print(f"####################################################")
    print(f"### lgbm_dummy; execution time:{end-start}")

    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print('F1 score: %.3f' % score)
    print('MSE: ', MSE)
    print('RMSE: ', RMSE)
    print('R2score :', R2score)
    print(classification_report(y_test, ypredl))


