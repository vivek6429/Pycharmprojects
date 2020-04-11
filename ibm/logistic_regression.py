
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
#metrics -- group of methords already present inside
# load the diabetes dataset
diabetes=datasets.load_diabetes()
# use only one feature
diabetes_x = diabetes.data[:,np.newaxis,2]

#split data into training and testing sets
diabetes_x_train = diabetes_x[:-250]
diabetes_x_test = diabetes_x[-250:]

#split data into training and testing sets
diabetes_y_train = diabetes.target[:-250]
diabetes_y_test = diabetes.target[-250:]

#leniar regression object scikit already has these functions
regr=linear_model.LinearRegression()

# Training the model using training sets
regr.fit(diabetes_x_train,diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred =regr.predict(diabetes_x_test)

# The coefficients
print('coefficients: \n',regr.coef_) #b0

# The mean square errorr
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test,diabetes_y_pred))

# Explained variance score 1 is perfect prediction
print("Variance  score: %.2f" % r2_score(diabetes_y_test,diabetes_y_pred))
##?how much percentage is close to line
# Plot outputs
plt.scatter(diabetes_x_test,diabetes_y_test,color='black')
plt.plot(diabetes_x_test,diabetes_y_pred,color='red',linewidth=3)
plt.xticks(()) # to hide axis
plt.yticks(())
plt.show()


# conclusion
# as the dtaing data is increased variance score decreasd and
# machine can do better prediction, accuracy increased