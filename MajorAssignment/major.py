import os
import csv
from matplotlib.pyplot import table
from numpy import fix
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here,"winequality-white.csv")
attributes, fixed_acidity, volatile_acidity, critic_acid, reisdual_sugar, chlorides, free_sulfure_dioxide, total_sulfure_dioxide, density, pH, sulphates, alcohol = ([] for _ in range(12))
with open(filename) as file:
    semicolon_reader = csv.reader(file, delimiter=";")
    semicolon_reader.__next__()
    for rows in semicolon_reader:
        fixed_acidity.append(float(rows[0]))
        volatile_acidity.append(float(rows[1]))
        critic_acid.append(float(rows[2]))
        reisdual_sugar.append(float(rows[3]))
        chlorides.append(float(rows[4]))
        free_sulfure_dioxide.append(float(rows[5]))
        total_sulfure_dioxide.append(float(rows[6]))
        density.append(float(rows[7]))
        pH.append(float(rows[8]))
        sulphates.append(float(rows[9]))
        alcohol.append(float(rows[10]))
attributes = [fixed_acidity, volatile_acidity, critic_acid, reisdual_sugar, chlorides, free_sulfure_dioxide, total_sulfure_dioxide, density, pH, sulphates, alcohol]
bucket_size = list()
for each_attr in attributes:
    bucket_size.append((max(each_attr) - min(each_attr)) / 30)
print(bucket_size)
print(attributes)