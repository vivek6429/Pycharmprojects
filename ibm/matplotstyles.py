import numpy as np
list=[1,2,3,4]
arr=np.array(list)
import matplotlib.pyplot as plt

# for style in plt.style.available:
#     print(style)

np.random.seed(119680801)
def plot_scatter(ax,prng,nb_samples=100):
    