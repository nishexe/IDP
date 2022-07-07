def rosenbrock(x, y):
    return ((1 - x) ** 2) + (100 * ((y - (x ** 2)) ** 2))
def gradient(f, x, y, h=0.001, k=0.001):
    return [(f(x+h, y) - f(x, y)) / h, (f(x, y+k) - f(x, y)) / k]
def main():
    x, y = 1, 2
    res = gradient(rosenbrock, x, y)
    print(res)
if __name__ == "__main__":
    main()