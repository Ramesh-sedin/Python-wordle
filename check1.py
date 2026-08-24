import json

class GameHistory:
    def __init__(self, fileName = "history.json"):
        self.fileName = fileName
        self.games = []
        self.load()

    def load(self):
        try:
            with open(self.fileName, 'r') as file:
                self.games = json.load(file)
        except FileNotFoundError:
            self.games = []
            self.save()

    def save(self):
        with open(self.fileName, 'w') as file:
            json.dump(self.games, file, indent=4)

    def add_game(self, won, attempt, word):
        game = {
            "won": won,
            "attempt": attempt,
            "word": word
        }
        self.games.append(game)
        self.save()

    @property
    def total_games(self):
        return len(self.games)

    @property