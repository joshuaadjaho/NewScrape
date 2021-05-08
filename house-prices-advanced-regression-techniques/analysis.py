import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_csv('test.csv')

# # street_type = df['Street'].unique()
# # number_street = df['Street'].value_counts()

# # SHOW ALL COLUMNS 
# #pd.set_option("display.max.columns", None)

# x= df['GarageCars']
# y=df['GarageArea']

# p1 = np.polyfit(x,y,1)

# df.plot(x, polyval(p1,x))
# df.plot(x, y, kind='scatter')


# plt.show()


x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1]

curve = np.polyfit(x,y,2)
# poly = np.poly1d(curve)
# print(poly)

