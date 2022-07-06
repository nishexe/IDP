import random
from sys import getsizeof
numeric_string = "1234567890"
alphabet_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphanumeric = numeric_string + alphabet_string
test_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
def generate_password(length,num_of_passwords,file):
    password = ""
    for x in range(num_of_passwords):
        generated = random.choices(alphanumeric,k=length)
        password = password.join(generated)
        if x != num_of_passwords - 1:
            file.write(password + "\n")
        else:
            file.write(password)
        password = ""
    #print(f"Successfully written to {file}")
    file.close()
    
def main():
    file = open("MyPasswords.txt","w+")
    length = int(input("Enter password length: "))
    num_of_passwords = int(input("Enter no. of passwords required: "))
    generate_password(length,num_of_passwords,file)

    #debugging
    #print(f"Size of numeric_string: {getsizeof(numeric_string)}")
    #print(f"Size of alphabet_string: {getsizeof(alphabet_string)}")
    #print(f"Size of alphanumeric_string: {getsizeof(alphanumeric)}")
    #print(f"Size of test_string: {getsizeof(test_string)}")

if __name__ == "__main__":
    main()
