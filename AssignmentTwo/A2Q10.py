import math
import matplotlib.pyplot as plt
def normal_cdf(x, mu = 0, sigma = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def main():
    x = [z/10 for z in range(-100,100)]
    a, b, c, d = ([] for _ in range(4))
    for i in x:
        a.append(normal_cdf(i, 1, 1))
        b.append(normal_cdf(i, 2, 2))
        c.append(normal_cdf(i, 3, 3))
        d.append(normal_cdf(i, 4, 4))

    plt.plot(a,color='#99b998',linestyle = "dashdot")
    plt.plot(b,color='#fdceaa',linestyle = "dashed")
    plt.plot(c,color='#eb4960',linestyle = "dotted")
    plt.plot(d,color= 'teal' ,linestyle = "solid")
    plt.title("Normal PDF with same μ & σ values.")
    plt.legend(["μ : 1 σ: 1", "μ : 2 σ: 2", "μ : 3 σ: 3", "μ : 4 σ: 4"])
    
    plt.show()
    
if __name__ == "__main__":
    main()