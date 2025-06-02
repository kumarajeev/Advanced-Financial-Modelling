import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Pie chart
set1 = np.array([25, 17, 5, 53])
plt.pie(set1)
plt.title('Pie chart')
plt.show()


#Linear graph

set1 = [3, 8, 12, 5, 10, 1]
set2 = [7, 15, 19, 25, 4, 9]

plt.plot(set1, set2)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Linear graph')
plt.show()


#Histogram

set1 = np.random.normal(50, 75, 150,)
plt.hist(set1)
plt.title('Histogram')
plt.show()


