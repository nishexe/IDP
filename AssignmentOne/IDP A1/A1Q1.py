salaries = [(83000, 8.7), (88000, 8.1), (48000, 0.7),(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000,10),(48000, 1.9), (63000, 4.2)]
dict = dict()
for i in salaries:
    if i[1]<2:
        if "less then 2" not in dict:
            dict["less then 2"] = [i[0]]
        else:
            dict["less then 2"] += [i[0]]
    elif 2<i[1] and i[1]>5:
        if "between two and five" not in dict:
            dict["between two and five"] = [i[0]]
        else:
            dict["between two and five"] += [i[0]]
    elif i[0]>5:
        if "more than five" not in dict:
            dict["more than five"] = [i[0]]
        else:
            dict["more than five"] += [i[0]]
for i in dict:
    dict[i]=(sum(dict[i])/len(dict[i]))
print(dict)