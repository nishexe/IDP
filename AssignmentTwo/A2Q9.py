import math
from matplotlib import style
import matplotlib.pyplot as plt
SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x, mu = 0, sigma = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

def main():
    x = [z/10 for z in range(-100,100)]
    a, b, c, d = ([] for _ in range(4))
    for i in x:
        a.append(normal_pdf(i, 0, 1))
        b.append(normal_pdf(i, 0, 2))
        c.append(normal_pdf(i, 0, 0.5))
        d.append(normal_pdf(i, -1, 1))

    plt.plot(a,color='#99b998',linestyle = "dashdot")
    plt.plot(b,color='#fdceaa',linestyle = "dashed")
    plt.plot(c,color='#eb4960',linestyle = "dotted")
    plt.plot(d,color= 'teal' ,linestyle = "solid")
    plt.title("Normal PDF with different μ & σ values.")
    plt.legend(["μ : 0 σ: 1", "μ : 0 σ: 2", "μ : 0 σ: 0.5", "μ : -1 σ: 1"])
    
    plt.show()
    
if __name__ == "__main__":
    main()