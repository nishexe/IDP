import string
def find_freq(file) -> dict:
    all_lines = "".join(file.read()).lower()
    freq = {}
    for x in all_lines:
        if x not in string.ascii_lowercase:
            pass
        else:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
    return freq

def total_chars(file) -> int:
    all_lines = "".join(file.read()).lower()
    num_of_chars = 0
    for x in all_lines:
        if x not in string.ascii_lowercase:
            pass
        else:
            num_of_chars += 1
    return num_of_chars

def unique_chars(file) -> int:
    all_lines = "".join(file.read()).lower()
    ignore_chars = ["\n"," ",'""',"''","(",")","[","]","{","}","<",">","."]
    unique_characters = set()
    for z in all_lines:
        if z in ignore_chars:
            pass
        else:
            unique_characters.add(z)
    return len(unique_characters)

def compare_freq(freq_one, freq_two):
    x=set(freq_two)-set(freq_one)
    for key,val in freq_one.items():
        if key not in freq_two:
            print("The char "+key+" is more in MyText1.txt than MyText2.txt")
            continue
        if(freq_one[key]>freq_two[key]):
            print("The char "+key+" is more in MyText1.txt than MyText2.txt")
        elif(freq_one[key]<freq_two[key]):
            print("The char "+key+" is less in MyText1.txt than MyText2.txt")
        elif(freq_one[key]==freq_two[key]):
            print("The char "+key+" is equal in MyText1.txt and MyText2.txt")
        for key in x:
            print("The char "+key+" is less in MyText1.txt than MyText2.txt")

def main():
    try:
        file_one = open("MyText1.txt","r")
        file_two = open("MyText2.txt","r")
    except FileNotFoundError:
        print("File Not Found!")
        
    total_chars_one = total_chars(file_one)
    total_chars_two = total_chars(file_two)
    if total_chars_one > total_chars_two:
        print("File MyText1 contains more characters than MyText2.")
    elif total_chars_one == total_chars_two:
        print("File MyText1 contains equal characters to MyText2.")
    else:
        print("File MyText1 contains less characters than MyText2.")
    
    file_one = open("MyText1.txt","r")
    file_two = open("MyText2.txt","r")
    
    unique_chars_one = unique_chars(file_one)
    unique_chars_two = unique_chars(file_two)
    if unique_chars_one > unique_chars_two:
        print("File MyText1 contains more unique characters than MyText2.")
    elif unique_chars_one == unique_chars_two:
        print("File MyText1 contains equal unique characters to MyText2.")
    else:
        print("File MyText1 contains less unique characters than MyText2.")

    file_one = open("MyText1.txt","r")
    file_two = open("MyText2.txt","r")
    freq_one = find_freq(file_one)
    freq_two = find_freq(file_two)
    compare_freq(freq_one,freq_two)

if __name__ == "__main__":
    main()