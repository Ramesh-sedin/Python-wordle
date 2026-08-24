MAX_GUESS = 6
WORD_LENGTH = 5

class GuessResult:
    def __init__(self, guess, result):
        self.guess = guess
        self.result = result

    def __str__(self):
        sentence = "  ".join(self.guess)

        symbols = {
            "correct": "✓",
            "present": "~",
            "absent": "✗"
        }

        result = "  ".join(symbols[i] for i in self.result)

        return f"{sentence} \n\n {result}"

def evaluate_guess(secret: str, guess: str) -> GuessResult:
    result = [None] * WORD_LENGTH
    remaining = list(secret)

    for index in range(WORD_LENGTH):
        if guess[index] == secret[index]:
            result[index] = "Correct"
            remaining[index] = None

    for index in range(WORD_LENGTH):
        if result[index] is not None:
            continue

        if guess[index] in remaining:
            result[index] = 'present'
            remaining[remaining.index(guess[index])] = None

        else:
            result[index] = 'absent'

    return GuessResult(guess, result)


class Game:
    def __init__(self, secret, words):
        self.secret = secret
        self.words = words
        self.guesses = []

    def make_guess(self, word: str) -> GuessResult:
        if self.is_over:
            raise ValueError("Game is already over")

        if len(word) != WORD_LENGTH:
            raise ValueError("Enter exactly 5 character")

        if word not in self.words:
            raise ValueError("Guess is not in the word list.")

        result = evaluate_guess(self.secret, word)

        self.guesses.append(result)

        return result

    @property
    def is_won(self):
        return bool(self.guesses) and self.guesses[-1].guess == self.secret

    def is_over(self):
        return self.is_won or len(self.guesses) >= MAX_GUESS

    def __str__(self) -> str:
        board = "\n\n".join(str(guess) for guess in self.guesses)
        remaining = MAX_GUESS - len(self.guesses)

        return f"{board} \n {remaining}chances left"