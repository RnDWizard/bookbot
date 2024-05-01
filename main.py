with open(r'/home/rndwizard/coding_projects/bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()


words = file_contents.lower()

    #  Word Count
words_list = words.split()
word_count = len(words_list)

    # Dictionary Count Function
alphabet_dict = {}
for letter in words:
    if letter.isalpha():
        if letter in alphabet_dict:
            alphabet_dict[letter] += 1
        else:
            alphabet_dict[letter] = 1

# print(alphabet_dict)


print("--- Begin report of books/frankenstein.txt ---")
print(str(word_count) +  " words were found in the document")
for i in alphabet_dict:
    print(f"The Letter {i} appears {alphabet_dict[i]} times")
print("---End Report---")