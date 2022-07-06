try:
    file = open("MyText.txt","r")
except FileNotFoundError:
    print("File Not Found")
all_lines = "".join(file.read()).lower()
ignore_chars = ["\n"," ",'""',"''","(",")","[","]","{","}","<",">","."]
unique_characters = set()
for z in all_lines:
    if z in ignore_chars:
        pass
    else:
        unique_characters.add(z)
print("Unique Characters Are:",unique_characters)
freq = {}
for x in all_lines:
    if x in ignore_chars:
        pass
    else:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
for key, value in freq.items():
    print("The character " +'"'+key+'"',"is present",value,"times")
file.close()