import math
def is_perfect_square(num) -> bool:
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return True
    else:
        return False

def sum_of_digits(num) -> int:
    sum = 0
    for x in str(num):
        sum += int(x)
    return sum

def func(_range) -> list:
    num_list = list()
    for x in range(_range):
        if is_perfect_square(x) and sum_of_digits(x) < 10:
            num_list.append(x)
    return num_list        

def main():
    _range = int(input("Enter the range: "))
    print("List of perfect squares in the range",_range,"with sum of digits < 10: ",func(_range))

if __name__ == "__main__":
    main()
