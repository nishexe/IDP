import matplotlib.pyplot as plt
max=[17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min= [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
month=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]
plt.scatter(month,max,color="teal",marker="o")
plt.scatter(month,min,color="skyblue",marker="s")
plt.legend(["Max values","Min values"])
plt.xlabel("Month")
plt.ylabel("Temp")
plt.title("Temp vs Month")
plt.show()
