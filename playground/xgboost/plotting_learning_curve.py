#https://vitalflux.com/learning-curves-explained-python-sklearn-example/

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np


# Load Breast Cancer Dataset
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target

#print(np.shape(X)) #(569, 30)
#print(np.shape(y)) #(569,)
print(X[0:20,0])

#print(y[0:20])

# Create training and test split
X_train, X_test, y_train, y_test = \
    train_test_split(X, 
                     y, 
                     test_size=0.3, 
                     stratify=y, 
                     random_state=1)

#print(np.shape(y_train)) #(398,)
#print(np.shape(y_test)) #(171,)
#print(np.shape(X_test)) #(171,30)


# Create a pipeline; This will be passed as an estimator to learning curve method
pipeline = make_pipeline(
                        StandardScaler(),
                        LogisticRegression(
                                            penalty='l2', 
                                            solver='lbfgs', 
                                            random_state=1, 
                                            max_iter=10000
                                            )
                        )

#print(type(pipeline)) #<class 'sklearn.pipeline.Pipeline'>
#print(pipeline) #

# Use learning curve to get training and test scores along with train sizes
cv_values = 10
train_size_array=np.linspace(0.1, 1.0, 10),

train_sizes, train_scores, test_scores = \
    learning_curve(
                    estimator=pipeline, 
                    X=X_train, 
                    y=y_train,
                    cv=cv_values, 
                    train_sizes=train_size_array,
                    n_jobs=1
                    )


#print(np.shape(train_sizes)) #(10,)
#print(np.shape(train_scores)) #(10,10)
#print(np.shape(test_scores)) #(10,10)
#print(train_sizes)
#print(train_scores)
#print(test_scores)

# Calculate training and test mean and std
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

#print(train_mean)
#print(train_std)
#print(train_mean, train_std, test_mean, test_std)


## Plot the learning curve
plt.plot(train_sizes, train_mean, color='blue', marker='o', markersize=5, label='Training Accuracy')
plt.fill_between(train_sizes, train_mean + train_std, train_mean - train_std, alpha=0.15, color='blue')
plt.plot(train_sizes, test_mean, color='green', marker='+', markersize=5, linestyle='--', label='Validation Accuracy')
plt.fill_between(train_sizes, test_mean + test_std, test_mean - test_std, alpha=0.15, color='green')
plt.title('Learning Curve')
plt.xlabel('Training Data Size')
plt.ylabel('Model accuracy')
plt.grid()
plt.legend(loc='lower right')
plt.show()



