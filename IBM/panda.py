import pandas as pd
data=pd.read_csv('dataset1.csv')


print("Shape:", data.shape)
print("\nFeatures:", data.columns)
X = data[data.columns[0:2]]
y = data[data.columns[-1]]
print("\nX matrix:\n", X.head())
print("\nY vector:\n", y.head())
