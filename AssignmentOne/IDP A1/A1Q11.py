import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10,11,12]
max = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.plot(x,max, 'm-.', x, min, 'c:')
plt.show()