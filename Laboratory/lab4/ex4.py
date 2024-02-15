f=open('ex4.txt')
all_file = f.read()
list = all_file.split("\n")
string = " ".join(list)
list = string.split(" ")

words_frequency = {}

for word in list:
    words_frequency.update({word:list.count(word)})

print(words_frequency)