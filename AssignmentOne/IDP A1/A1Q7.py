import string
import matplotlib.pyplot as plt
try:
    file = open("MyText.txt","r")
except FileNotFoundError:
    print("File Not Found")
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
print(freq)
letters = list(freq.keys())
freq = list(freq.values())
plt.bar(letters, freq, color ='skyblue',width = 0.5)
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Frequencies Of Various Alphabets")
plt.show()