import math
def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu = 0, sigma = 1,tolerance = 0.00001) -> float:
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z = -10.0                     
    hi_z  =  10.0                      
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     
        mid_p = normal_cdf(mid_z)      
        if mid_p < p:
            low_z = mid_z           
        else:
            hi_z = mid_z               
    return mid_z

def main():
    print(inverse_normal_cdf(0.5))

if __name__ == "__main__":
    main()