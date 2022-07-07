def vector_mean(v):
    summ = [sum(vi[i] for vi in v)for i in range(len(v[0]))]
    return [1/len(v) * i for i in summ]
def main():
    print(vector_mean([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == "__main__":
    main()