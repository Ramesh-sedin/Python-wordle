import json


class GameHistory:
    def __init__(self, filename="history.jsonl"):
        self.filename = filename
        self.games = []
        self.load()
            
    def load(self):
        try:
            with open(self.filename, "r") as file:
                self.games = [json.loads(line) for line in file]
        except FileNotFoundError:
            self.games = []

    
    def save(self, game):
        with open(self.filename, "a") as file:
            json.dump(game, file)
            file.write("\n")

    def add_game(self, won, attempts, word):
        game = {
            "won": won,
            "attempts": attempts,
            "word": word
        }
        self.games.append(game)
        self.save(game)

    @property
    def total_games(self):
        return len(self.games)

    @property
    def total_wins(self):
        return sum(game["won"] for game in self.games)

    @property
    def win_percentage(self):
        if self.total_games == 0:
            return 0
        return (self.total_wins / self.total_games) * 100

    @property
    def current_streak(self):
        streak = 0
        for game in reversed(self.games):
            if game["won"]:
                streak += 1
            else:
                break

        return streak

    @property
    def best_streak(self):
        best = 0
        current = 0

        for game in self.games:
            if game["won"]:
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best

    def __str__(self) -> str:
        return (
            f"Games played: {self.total_games}\n"
            f"Wins: {self.total_wins}\n"
            f"Win percentage: {self.win_percentage:.1f}%\n"
            f"Current streak: {self.current_streak}\n"
            f"Best streak: {self.best_streak}"
        )