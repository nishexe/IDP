# import matplotlib.pyplot as plt
# male_age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
# female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]
# plt.hist(male_age,edgecolor = "black",color="skyblue")
# # plt.hist(female_age,edgecolor = "black",color="pink")
# plt.xlabel("Age Range ")
# plt.ylabel("#of Males")
# plt.title("Male Age")
# plt.show()

import matplotlib.pyplot as plt
male_age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]
plt.hist(female_age,edgecolor = "black",color="pink")
plt.xlabel("Age Range ")
plt.ylabel("#of  Females")
plt.title("Female Age")
plt.show()