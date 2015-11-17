input_file = open("input.txt", 'r')

unique_words = set()

for line in input_file:
    words = line.strip().split()
    for word in words:
        unique_words.add(word)

print(len(unique_words))