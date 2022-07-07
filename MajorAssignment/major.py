import os
import csv
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here,"winequality-white.csv")
def mean(vec : list) -> float:
    return sum(vec) / len(vec)

def median(vec : list) -> int:
    vec = sorted(vec)
    if len(vec) % 2 == 0:
        return mean(vec[(len(vec) - 1) // 2 : ((len(vec) - 1) // 2) + 2 ])
    else:
        return (vec[(len(vec) - 1) // 2])

def mode(vec : list) -> float:
    freq = Counter(vec)
    max_count = max(freq.values())
    return [k for k,v in freq.items() if v == max_count]

def variance(vec : list) -> float:
    _mean = mean(vec)
    res = sum((i - _mean) ** 2 for i in vec) / len(vec)
    return res

def main():
    header = list()
    attributes, fixed_acidity, volatile_acidity, critic_acid, reisdual_sugar, chlorides, free_sulfure_dioxide, total_sulfure_dioxide, density, pH, sulphates, alcohol = ([] for _ in range(12))
    with open(filename) as file:
        semicolon_reader = csv.reader(file, delimiter=";")
        header = semicolon_reader.__next__()
        header.pop()
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
    b = [6, 7, 3, 9, 10, 15]
    print(variance(b))

if __name__ == "__main__":
    main()