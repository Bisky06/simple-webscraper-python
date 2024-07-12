import matplotlib.pyplot as plt
import numpy as np

from package.functions import filter
from scraper import end_result

e = end_result
x = filter(e)

name = np.array([x[0],x[2],x[4],x[6]])
value = np.array([x[1],x[3],x[5],x[7]])
plt.bar(name,value, color = '#b3bef0', width = 0.5)
plt.title('Top Searched Keywords On Google Globally')
plt.xlabel('Top Keywords')
plt.ylabel('Global Search Volume')
plt.savefig('./KS/data/plot.png', bbox_inches = 'tight')
