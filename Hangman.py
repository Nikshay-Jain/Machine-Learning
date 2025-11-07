import random

def choose_random_word():
    words = ["apple", "banana", "orange", "grape", "watermelon", "strawberry", "pineapple", "mango", "cherry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_possible_words(word_list, guessed_letters):
    possible_words = []
    for word in word_list:
        if all(letter in guessed_letters for letter in word):
            possible_words.append(word)
    return possible_words

def get_most_frequent_letter(word_list, guessed_letters):
    all_letters = "".join(word_list)
    letter_frequency = {}
    for letter in all_letters:
        if letter not in guessed_letters:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
    if not letter_frequency:
        return random.choice(all_letters)
    return max(letter_frequency, key=letter_frequency.get)

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_list = choose_random_word()
    attempts = 0

    print("Welcome to Hangman!")

    while attempts < max_attempts:
        if not guessed_letters:
            guess = random.choice(word_list)
        else:
            possible_words = get_possible_words(word_list, guessed_letters)
            if possible_words:
                guess = get_most_frequent_letter(possible_words, guessed_letters)
            else:
                break

        guessed_letters.append(guess)

        if guess not in word_list:
            attempts += 1
