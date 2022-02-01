"""One step closer to Wordle."""
__author__ = "730521885"

seceret_word = "python"
user_guess = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i = int(0) #box check index
emoji = ""
guess_exist = bool(False)
idx = int(0) #other match

user_guess = input("What is yoru 6-letter guess? ")

while len(user_guess) != len(seceret_word):
    user_guess = input("That was not 6 letters! Try again: ")
while i < len(seceret_word):
    if seceret_word[i] == user_guess[i]:
        emoji = emoji + GREEN_BOX
    else:
        while guess_exist == False and i < idx<len(seceret_word):
            if seceret_word[idx] == user_guess[idx]:
                guess_exist = True
            else: 
                idx += 1
        if guess_exist == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    i += 1

print(emoji)