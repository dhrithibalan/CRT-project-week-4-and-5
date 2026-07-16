from random import choice

# 1. print "let's play hangman"
print("Let's play Hangman!")

# 2. create wordbank
wordfile = open("wordbank.txt", "r")
wordbank = wordfile.read().splitlines()  # list of words: ['word1', 'word2', 'word3', 'etc']
wordfile.close()

# 3. make dashes for num letters
def make_dashes(word):
    return "-" * len(word)

def play_hangman():
    # pick random word from word bank
    secret_word = choice(wordbank).lower()
    # make the dashes a list so it can be replaced by letters later
    display = list(make_dashes(secret_word))
    # main variables
    guessed_letters = ''
    guesses_left = 6
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # main loop
    while guesses_left > 0:
        # loops through word, prints letter if guessed, if not dash
        display = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += '- '

        # print current word + guesses
        print(f"\nWord: {display}")
        print(f"\nGuesses remaining: {guesses_left}")

        # check if player won, so no more dashes
        if '-' not in display:
            print("You won!")
            break

        guess = input("Guess a letter: ").lower()

        # other input possibilities: not one letter and not in alphabet
        if len(guess) != 1 or guess not in alphabet:
            print("Please enter one letter from a-z")
            continue

        if guess in guessed_letters:
            print("You already guessed that")
            continue

        guessed_letters += guess

        if guess not in secret_word:
            print(f"{guess} is not in the word")
            guesses_left -= 1
    else:
        print(f"Game over. The word was {secret_word}")

play_hangman()
