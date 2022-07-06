from matplotlib import pyplot as plt
mentions = [500, 505]
years = [2017, 2018]
plt.bar(range(len(years)),mentions)
plt.ylim(bottom=0)
plt.ylabel("Mentions")
plt.xticks(range(len(years)),years)
plt.show()