# xgboost.XGBClassifier

## Installing Dependencies
Install [eVE](../../../pyVEs/eVE.yml) virtual environment

## Running notebooks
```
mamba activate eVE
python *.py
```


## logs
* Using `xgboost_parameters.py`
```
#Default parameters
Accuracy: 72.83%
F1 score: 0.623
MSE:  0.27165354330708663
RMSE:  0.5212039363887102
R2score : -0.17592592592592582

#n_es2000;lr0.001;boostergbtree;devicecpu
Accuracy: 75.59%
F1 score: 0.648
MSE:  0.2440944881889764
RMSE:  0.4940591950252281
R2score : -0.05662909286097695

```




## References
https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier  
https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html   
https://stackoverflow.com/questions/34674797/xgboost-xgbclassifier-defaults-in-python 
https://machinelearningmastery.com/extreme-gradient-boosting-ensemble-in-python  



