def rosenbrock(x, y):
    return ((1 - x) ** 2) + ((y - (x ** 2)) ** 2)
def gradient(f, x, y, h=0.001, k=0.001):
    return [(f(x+h, y) - f(x, y)) / h, (f(x, y+k) - f(x, y)) / k]
def magnitude(v):
    return sum(vi ** 2 for vi in v) ** 0.5
def gradientDescent(f, x0, y0, alpha=0.05, threshold=0.000001):
    iteration = 0
    x, y = x0, y0
    grad = gradient(f, x, y)
    while magnitude(grad) >= threshold and iteration < 1000:
        x = x - (alpha * grad[0])
        y = y - (alpha * grad[1])
        grad = gradient(f, x, y)
        print(iteration, [x, y])
        iteration += 1
    return x, y
def main():
    x0, y0 = 0, 0
    minima = gradientDescent(rosenbrock, x0, y0)
    print(f'Point of minima: {minima[0], minima[1]}')
if __name__ == '__main__':
    main()