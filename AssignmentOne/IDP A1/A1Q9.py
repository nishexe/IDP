import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10)
y0 = x*(np.sin(x))
y1 = x*x*(np.sin(x))
y2 = x*x*x*(np.sin(x))
y3 = x*x*x*x*(np.sin(x))
plt.plot(x,y0,x,y1,x,y2,x,y3)
plt.show()