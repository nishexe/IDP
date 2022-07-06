import random
numeric_string = "1234567890"
alphabet_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphanumeric = numeric_string + alphabet_string
def generate_password(length,num_of_passwords,file):
    password = ""
    for x in range(num_of_passwords):
        generated = random.sample(alphanumeric,length)
        password = password.join(generated)
        file.write(password + "\n")
        password = ""
    file.close()
    
def main():
    file = open("MyPasswords.txt","w+")
    length = int(input("Enter password length: "))
    num_of_passwords = int(input("Enter no. of passwords requrired: "))
    generate_password(length,num_of_passwords,file)
    
if __name__ == "__main__":
    main()
