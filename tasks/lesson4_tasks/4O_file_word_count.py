input_file = open("input.txt", 'r')

word_count_dict = {} # {'word1': n1, 'word2': n2}

for line in input_file:
    words = line.strip().split(" ")
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
            
print(word_count_dict)

print(len(word_count_dict))