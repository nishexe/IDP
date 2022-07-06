from collections import defaultdict
salaries_and_tenures = [
(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience > 8.0:
        return "paid"
    else:
        return "unpaid"

def main():
    salary_per_tenure = defaultdict(list)
    for salary, tenure in salaries_and_tenures:
        paid_or_unpaid = predict_paid_or_unpaid(tenure)
        salary_per_tenure[tenure].append(paid_or_unpaid)
    res={}
    for key, value in salary_per_tenure.items():
        res[key]=value[0]
    print(res)

if __name__ == "__main__":
    main()
