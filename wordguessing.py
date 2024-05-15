import random

user_name = input("What is your name? ")

print("Good Luck ! ", user_name)

words_list = ['rainbow', 'computer', 'science', 'programming',
              'python', 'mathematics', 'player', 'condition',
              'reverse', 'water', 'board', 'geeks']

selected_word = random.choice(words_list)

print("Guess the characters")

user_guesses = ''

max_turns = 12

while max_turns > 0:
    failed_attempts = 0

    for character in selected_word:
        if character in user_guesses:
            print(character, end=" ")
        else:
            print("_")

            failed_attempts += 1

    if failed_attempts == 0:
        print("You Win")
        print("The word is: ", selected_word)
        break

    print()
    user_input = input("Guess a character:")

    user_guesses += user_input

    if user_input not in selected_word:
        max_turns -= 1
        print("Wrong")
        print("You have", + max_turns, 'more guesses')

        if max_turns == 0:
            print("You Loose")
