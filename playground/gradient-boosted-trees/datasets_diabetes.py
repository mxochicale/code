#https://colab.research.google.com/gist/DeepakNair93/573cc1d52f497c685b7a96ce37838dd5/untitled0.ipynb#scrollTo=kdHS_7x78c0M

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
#X, y = load_diabetes(return_X_y=True)
#Samples total 442
#Dimensionality 10
#Features real, -.2 < x < .2
#Targets integer 25 - 346

#print(diabetes.DESCR)
print(diabetes.feature_names)   #checking the feature names
print(diabetes.data.shape)  #checking the shape of data
print(diabetes.target.shape)
#print(diabetes.target)
print(diabetes.target[:3])


db_df = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
db_df['Progression'] = diabetes.target #new column name 'Progression'
#print(db_df.isna().sum())
print(db_df.describe())
print(db_df.info())

corr = db_df.corr()
plt.subplots(figsize=(8,8))
sns.heatmap(corr,cmap= 'RdYlGn',annot=True)
plt.show()


#This plot shows the linear correlation between the variables within themselves & also variables with the target 'Progression'. 
#This could be a phase where the variables which are multicollinear can be eliminated. 
# https://medium.com/@hammad.ai/3-ways-to-detect-multicollinearity-in-your-dataset-6ee1776b7aa8


