import math
def normal_cdf(x, mu= 0, sigma= 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def main():
    print(normal_cdf())
    
if __name__ == "__main__":
    main()