import random

color_words = '''red pink orange yellow purple green blue brown indigo gray black white cyan coral
coffee aqua amber olive teal'''
fruit_words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
color_words = color_words.split(" ")
fruit_words = fruit_words.split(" ")

play = True

while play:
    word = random.choice(color_words + fruit_words)
    lost_word = word

    guessed_word = []
    lives = 3

    print("GUESS THE WORD \t \t Total lives: {}".format(lives))
    if word == "orange":
        print("Hint: It's a color and a fruit")
    elif word in color_words:
        print("Hint: It's a color")
    else:
        print("Hint: It's a fruit")
    print()

    for i in word:
        guessed_word.append("_ ")
    print("".join(guessed_word))

    while "_ " in guessed_word and lives > 0:
        letter = input("\t Enter a letter:")
        if letter in word:
            i = word.index(letter)
            guessed_word[i] = letter
            print("".join(guessed_word))        
            word = word.replace(letter, "-",1)
        else:
            lives = lives - 1
            print("Wrong guess - {} lives left".format(lives))
    print()

    if lives == 0:
        print("Lost the Game, the word was: ", lost_word)
    else:
        print("Won the Game")
        
    ans = input("Want to play again(y/n):")
    print()
    if ans.lower() == 'y':
        play = True
    else: 
        play = False