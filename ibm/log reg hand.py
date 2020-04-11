import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report , confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # used to make input value of same size eg 3 drawn in paint and in an photo
# will make all of them into a uniform dimension


# auto data,target func inside library
x, y = load_digits(return_X_y=True)
# split data
x_train, x_test, y_train, y_test =train_test_split(x, y, test_size=0.2, random_state=1)
print(x_test)

scaler = StandardScaler()  # an object created of StandardScaler class
x_train = scaler.fit_transform(x_train) # fitdimension according to common size
# fit transform will actually reduce the size of image to make unform dimension
x_test = scaler.transform(x_test) # transform will cut edges to make dimension niform
# no perfection in test data , train data perfect
model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state=0)
model.fit(x_train, y_train)




y_pred = model.predict(x_test)

# score  accuracy comparison
print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

print(classification_report(y_test, y_pred))

