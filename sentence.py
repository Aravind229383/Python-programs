sentence = input("Enter a sentence : ")

wordList = sentence.split(" ")
print("This sentence has ",len(wordList), "words")

digit_count = uppercase_count = lowercase_count = 0


for ch in sentence:
    if '0' <= ch <= '9':
        digit_count += 1
    elif 'A' <= ch <= 'Z':
        uppercase_count += 1
    elif 'a' <= ch <= 'z':
        lowercase_count += 1


print("This sentence has ",digit_count,"digits",uppercase_count,"upper case letters",lowercase_count,"lower case letters")