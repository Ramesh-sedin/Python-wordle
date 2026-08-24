MAX_GUESSES = 6
WORD_LENGTH = 5


class GuessResult:
    """result after the evaluation"""
    def __init__(self, guess, results):
        self.guess = guess
        self.results = results

    def __str__(self) -> str:
        my_guess = "  ".join(self.guess)

        symbols = {
            "correct": "✓",
            "present": "~",
            "absent": "✗"
        }

        result = "  ".join(symbols[i] for i in self.results)
        return f"{my_guess}\n{result}"


def evaluate_guess(secret: str, guess: str) -> GuessResult:
    """Evaluate a guess with secret word"""
    results = [None] * WORD_LENGTH
    remaining = list(secret)

    for index in range(WORD_LENGTH):
        if guess[index] == secret[index]:
            results[index] = "correct"
            remaining[index] = None

    for index in range(WORD_LENGTH):
        if results[index] is not None:
            continue

        if guess[index] in remaining:
            results[index] = "present"
            remaining[remaining.index(guess[index])] = None
        else:
            results[index] = "absent"
    return GuessResult(guess, results)


class Game:
    def __init__(self, secret, words):
        self.secret = secret
        self.words = words
        self.guesses = []

    def make_guess(self, word: str) -> GuessResult:
        if self.is_over:
            raise ValueError("The game is already over.")

        if len(word) != WORD_LENGTH:
            raise ValueError("Guess must be exactly 5 letters.")

        if word not in self.words:
            raise ValueError("Guess is not in the word list.")

        result = evaluate_guess(self.secret, word)
        self.guesses.append(result)
        return result

    @property
    def is_won(self):
        return bool(self.guesses) and self.guesses[-1].guess == self.secret

    @property
    def is_over(self):
        return self.is_won or len(self.guesses) >= MAX_GUESSES

    def __str__(self) -> str:
        board = "\n\n".join(str(guess) for guess in self.guesses)
        remaining = MAX_GUESSES - len(self.guesses)
        return f"Chances left: {remaining}\n\n{board}"