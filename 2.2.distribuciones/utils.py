import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style
style.use('seaborn-white')


def discrete_plot(data, alpha=.5):
    hist, edges = np.histogram(data,bins=np.arange(min(data),max(data)+2)-0.5)
    return plt.bar(edges[:-1], hist, align="edge", ec="k", alpha=alpha)