from math import sin
def func(x):
    return x ** 2 + sin(x)
def gradient(f, x, h=0.001):
    return (f(x+h) - f(x)) / h
def gradientDescent(f, x0, alpha=0.01, threshold=0.000001):
    iteration = 0
    x = x0
    grad = gradient(f, x)
    while grad >= threshold and iteration < 1000:
        x = x - (alpha * grad)
        grad = gradient(f, x)
        print(iteration, x)
        iteration += 1
    return x
def main():
    x0 = 2
    minima = gradientDescent(func, x0)
    print(f'Point of minima: {minima}')
if __name__ == "__main__":
    main()