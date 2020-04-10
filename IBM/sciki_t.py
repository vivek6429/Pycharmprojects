from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as k
from sklearn import metrics  # for calculating accuracy

iris = load_iris()
X = iris.data  # . data part contains independent variables
y = iris.target  # contains dependent variables only one column
# print(x)
# print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

print("\nFirst 5 rows of training data:\n", X_train[:5])
print("\nFirst 5 rows of test data:\n", X_test[:5])
print('Train Shape', X_train.shape)
print('Test Shape', X_test.shape)
print('Train Shape', y_train.shape)
print('Test Shape', y_test.shape)

knn = k(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
# accuracy calculation
print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))

# validation data
sample1 = [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]]
sample2 = [[1.0, 4.0, 3.0, 5.2], [3.1, 2.7, 0.7, 1.2]]
preds = knn.predict(sample2)
print(preds)
pred_species = [iris.target_names[p] for p in preds]
print("predictions:", pred_species)

# print("Feature names:", iris.feature_names)
# print("Target names:", iris.target_names)
# print("\nType of X is:", type(X))
# print("\nFirst5 rows of X:\n", X[0:5])
