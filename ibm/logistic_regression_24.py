import numpy as np
import matplotlib.pyplot as plt

t
csv
impor
import  math
def loadCSV(filename):
    with open(filename,"r") as csvfile:
        lines=csv.reader(csvfile)
        dataset=list(lines)
        for i in range(len(dataset)):
            dataset[i]=[float(x) for x in dataset]
    return np.array(dataset)

def plot_regression()
    x_0=np


def normalize(X):
    # basically dividing up
    # find min and max
    mins,maxs=np.min(x,axis=0),np.max(x,axis=0)
    rng=maxs-mins
    norm_x=1-((maxs-x)/rng)
    return norm_x

def grad_desc(x,y,beta,)
# Driver
dataset=LoadCSV("dataset1.csv")

x=normalize(dataset[:,:-1])
print(x)
y=dataset[:,-1]
