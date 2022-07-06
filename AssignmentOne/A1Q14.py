from matplotlib import pyplot as plt
test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
# Unequal Axes
plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Are Not Equal")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()
# Equal Axes
plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Are Equal")
plt.xlabel("test 1 grade")
plt.axis("equal")
plt.ylabel("test 2 grade")
plt.show()