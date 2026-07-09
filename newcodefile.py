from random import choice

# 1. print "let's play hangman"
print("Let's play Hangman!")

# 2. create wordbank
wordfile = open("wordbank.txt", "r")
wordbank = file.read().splitlines() # list of words: ['word1', 'word2', 'word3', 'etc']
wordfile.close()

# 3. make dashes for num letters
def make_dashes(word):
  return "-"*len(word)

