from math import erf, sqrt
def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2
def normal_approx_to_binomial(n, p):
    mu = n * p
    sigma = sqrt(n * p * (1-p))
    return mu, sigma
def normal_probability_above(x: float, mu: float = 0, sigma: float = 1):
    return 1 - normal_cdf(x, mu, sigma)
def normalProbabilityBetween(low: float, high: float, mu: float = 0, sigma: float = 1):
    return normal_cdf(high, mu, sigma) - normal_cdf(low, mu, sigma)
def main():
    n, p = 100, 0.6
    mu, sigma = normal_approx_to_binomial(n, p)
    x1 = 60
    x2 = (50, 70)
    prob1 = normal_probability_above(x1, mu, sigma)
    prob2 = normalProbabilityBetween(x2[0], x2[1], mu, sigma)
    print(f'X lies above 60: {prob1}\nX lies between 50 and 70: {prob2}')
if __name__ == '__main__':
 main()