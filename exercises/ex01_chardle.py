"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730521885"

five_char_word = str(input("Enter a 5-character word: "))
if len(five_char_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(five_char_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

single_char = str(input("Enter a single character: "))
if len(single_char) < 1:
    print("Error: Character must be a single character.")
    exit()
if len(single_char) > 1: 
    print("Error: Character must be a single character.")
    exit()

count = int(0)

diag_message = str("Searching for " + single_char + " in " + five_char_word)
print(diag_message)

if single_char in five_char_word:
    if single_char == five_char_word[0]:
        print(single_char + " found at index 0")
        count = count + 1
    if single_char == five_char_word[1]:
        print(single_char + " found at index 1")
        count = count + 1
    if single_char == five_char_word[2]:
        print(single_char + " found at index 2")
        count = count + 1
    if single_char == five_char_word[3]:
        print(single_char + " found at index 3")
        count = count + 1
    if single_char == five_char_word[4]:
        print(single_char + " found at index 4")
        count = count + 1
    print(str(count) + " instance of " + single_char + " found in " + five_char_word)
else:
    print("No instances of " + single_char + " in " + five_char_word)