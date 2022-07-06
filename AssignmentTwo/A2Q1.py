def vec_add() -> list:
    vec_one , vec_two = get_vectors()
    assert len(vec_one) == len(vec_two), "Vectors are of different length."
    print(f"Addition of {vec_one} + {vec_two} is : ", end = "")
    print([i + j for i, j in zip(vec_one, vec_two)])

def vec_sub() -> list:
    vec_one , vec_two = get_vectors()
    assert len(vec_one) == len(vec_two), "Vectors are of different length."
    print(f"Subtraction of {vec_one} - {vec_two} is : ", end = "")
    print([i - j for i, j in zip(vec_one, vec_two)])

def scalar_mul() -> list:
    vec_one = list()
    length_one = int(input("Enter size of the vector: "))
    print("Enter Vector Elements For The Vector: ")
    for _ in range(length_one):
        vec_one.append(int(input()))
    scalar_num = int(input("Enter the scalar number: "))
    print(f"Multiplying the Scalar {scalar_num} with {vec_one} is : ", end = "")
    print([scalar_num * i for i in vec_one])

def dot_prod() -> list:
    vec_one , vec_two = get_vectors()
    assert len(vec_one) == len(vec_two), "Vectors are of different length."
    print(f"Dot Product of {vec_one} (dot) {vec_two} is : ", end = "")
    print(sum(i * j for i, j in zip(vec_one, vec_two)))

def vec_length() -> int:
    vec = list()
    num_of_vec = int(input("How many vectors to compare?"))
    for x in range(num_of_vec):
        temp = list()
        print(f"Enter {x} Vector Elements, END = N")
        while(True):
            element = input("Enter Vector Elements: \n")
            if element == "N" :
                break;
            else:
                temp.append(element)
        vec.append(temp)
    for x in range(len(vec)):
        print(f"Length of {vec[x]} is {len(vec[x])}")

def get_vectors() -> list:
    vec_one = list()
    vec_two = list()
    length_one = int(input("Enter size of the first vector: "))
    length_two = int(input("Enter size of the second vector: "))
    print("Enter Vector Elements For First Vector: ")
    for x in range(length_one):
        vec_one.append(int(input()))
    print("Enter Vector Elements For Second Vector: ")
    for x in range(length_two):
        vec_two.append(int(input()))   
    return vec_one, vec_two

def main():
    while(True):
        print("\nENTER 1 FOR ADDITION")
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