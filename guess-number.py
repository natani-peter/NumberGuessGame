welcome_message = \
    """Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
        
Please choose the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)        
"""

print(welcome_message)

levels = {
    1: ("Easy", 10),
    2: ("Medium", 5),
    3: ("Hard", 3),
}


def get_user(number_range, prompt) -> int:
    difficulty = input(f"{prompt}")
    try:
        user_number = int(difficulty)
        if user_number in list(number_range):
            return user_number
        else:
            print("Invalid choice")
            user_number = get_user(number_range, prompt)

    except ValueError:
        print("Enter a valid number")
        user_number = get_user(number_range, prompt)

    return user_number


def get_my_number() -> int:
    import random
    return random.randint(2, 99)


def get_user_number() -> int:
    return get_user(range(2, 100), "Enter your guess: ")


def get_level() -> int:
    return get_user(range(1, 4), "Enter your choice: ")


def setChances(difficulty: int = 2) -> int:
    chances = 5

    if difficulty != 2:
        chances = 10 if difficulty == 1 else 3

    feedback(difficulty=difficulty)
    return chances


def feedback(guessed_number: int = 0, my_number: int = 0, difficulty=None):
    if difficulty:
        message = \
            f"""Great! You have selected the {levels[difficulty][0]} difficulty level.
Let us start the game!"""
        return print(message)

    if not guessed_number:
        return None

    if guessed_number == my_number:
        return True

    if guessed_number > my_number:
        return print(f"Incorrect! The number is less than by {guessed_number}.")

    return print(f"Incorrect! The number is greater than {guessed_number}.")


def final_congratulations(level, trials, attempts=0) -> None | bool:
    tail = f" in {trials} trials" if trials > 1 else " in your first attempt"
    if attempts:
        print(
            f"Congratulations! "
            f"You guessed the correct number in {attempts} attempts{tail} at {levels[level][0]} level.\n"
        )
        return True

    print(f"Failed! To guess the number in {levels[level][1]} chances, Another Trial !! \n")


def play(chances, my_number, level, trials):
    for chance in range(chances):
        guess_number = get_user_number()

        user_feedback = feedback(guessed_number=guess_number, my_number=my_number)

        if user_feedback:
            return final_congratulations(level=level, trials=trials, attempts=chance + 1)

    final_congratulations(level, trials=trials)


def play_game() -> None:
    level = get_level()
    chances = setChances(level)
    my_number = get_my_number()

    trials = 1
    while True:
        if not play(chances, my_number, level, trials=trials):
            trials += 1
            if input("Press  any to continue or [N] key to quit: ")[0].lower() != 'n':
                play(chances, my_number, level, trials=trials)
        break


def main():
    play_game()


if __name__ == "__main__":
    main()
