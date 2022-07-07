from math import erf, sqrt
def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2
def normalProbabilityAbove(x: float, mu: float = 0, sigma: float = 1):
    return 1 - normal_cdf(x, mu, sigma)
def twoSidedPValue(x: float, mu: float = 0, sigma: float = 1) -> float:
    if x >= mu:
        return 2 * normalProbabilityAbove(x, mu, sigma)
    return 2 * normal_cdf(x, mu, sigma)
def main():
    x = 110
    mu, sigma = 100, 5
    res = twoSidedPValue(x, mu, sigma)
    print(res)
if __name__ == "__main__":
    main()