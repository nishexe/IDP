import math
def func(x):
    return math.exp(x**2) + math.sin(x) - math.tan(x) + math.log(x)
def derivative(f, x, h=0.001):
    return (f(x+h) - f(x)) / h
def main():
    x = 1
    res = derivative(func, x)
    print(res)
if __name__ == "__main__":
 main()