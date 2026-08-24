import random
from game import Game
from history import GameHistory


def main():
    with open("words.txt") as file:
        words = [line.strip() for line in file]

    secret_word = random.choice(words)
    game = Game(secret_word, words)
    history = GameHistory()

    while not game.is_over:
        print(game)
        guess = input("Enter your guess: ").strip().lower()
        try:
            game.make_guess(guess)
        except ValueError as error:
            print(error)

    if game.is_won:
        print(f"you won it in {len(game.guesses)}/6!")
    else:
        print(f"Secret word is {game.secret_word}")

    history.add_game(
        game.is_won,
        len(game.guesses),
        game.secret
    )

    print(history)

if __name__ == "__main__":
    main()