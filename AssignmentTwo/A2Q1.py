def vec_add(vec_one, vec_two) -> list:
    assert len(vec_one) == len(vec_two), "Vectors are of different length."
    return [i + j for i, j in zip(vec_one, vec_two)]

def vec_sub(vec_one, vec_two) -> list:
    assert len(vec_one) == len(vec_two), "Vectors are of different length."
    return [i - j for i, j in zip(vec_one, vec_two)]

def scalar_mul(scalar_num, vec) -> list:
    return [scalar_num * i for i in vec]

def dot_prod(vec_one, vec_two) -> list:
    assert len(vec_one) == len(vec_two), "Vectors are of different length."
    return sum(i * j for i, j in zip(vec_one, vec_two))

def vec_length():
    pass

def main():
    while(True):
        print("ENTER 1 FOR ADDITION")
        print("ENTER 2 FOR SUBTRACTION")
        print("ENTER 3 FOR SCALAR MULTIPLICATION")
        print("ENTER 4 FOR DOT PRODUCT")
        print("ENTER 5 TO FIND LENGTH OF VECTORS")
        print("ENTER 0 TO EXIT \n")
        choice = int(input("ENTER CHOICE:"))
        if choice == 0:
            break
        elif choice == 1:
            vec_add()
        elif choice == 2:
            vec_sub()
        elif choice == 3:
            scalar_mul()
        elif choice == 4:
            dot_prod()
        elif choice == 5:
            vec_length()
        else:
            print("INVALID CHOICE! \n")

if __name__ == "__main__":
    main()