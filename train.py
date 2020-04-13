# Logistic Regression Iris Dataset

# Import the dependencies
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import json

# Load the data set
data = pd.read_csv('titanic.csv')
data.head()

variables = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
metric = ['Survived']

data = data[~data['Age'].isnull()]

# Prepare the training set
# X = feature values, all the columns except the last column
X = data[variables]
# y = target values, last column of the data frame
y = data[metric]

# Init model
model = LogisticRegression(C=1e5)
# Create an instance of Logistic Regression Classifier and fit the data.
model.fit(X, y)

# Export coefficients
coefficients = pd.concat([pd.DataFrame(variables), pd.DataFrame(np.transpose(model.coef_))], axis=1)
coefficients.columns = ['variable'] + y.columns.tolist()
intercept_dict = {'variable': 'intercept'}
intercept_dict.update(dict(zip(y.columns.tolist(), model.intercept_.tolist())))
coefficients = coefficients.append(intercept_dict, ignore_index=True)

coefficients_dict = coefficients.set_index('variable').to_dict()
with open('coefficients_dict.json', 'w') as outfile:
    json.dump(coefficients_dict, outfile, indent=2)
