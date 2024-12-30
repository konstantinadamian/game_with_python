retries = 3
magic_word = 'marshmallow'
letters = []

while retries != 0:
    user_input = input('give me a letter thats in side the magic_word : ')
    if user_input not in magic_word:
        retries -= 1
    else:
        letters.append(user_input)

    word_guessed = ""

    for letter in magic_word:
        if letter in letters:
            word_guessed += letter
        else:
            word_guessed += "_"
    if word_guessed == magic_word:
        print('You found the magic word!')
        break

    print(f"Word so far: {word_guessed}")
    print(f"Remaining retries: {retries}")

    if retries == 0:
        print('You lose!')