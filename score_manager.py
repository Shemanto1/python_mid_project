import json

class ScoreManager:
    def __init__(self, file="score.json"):
        self.file = file
        self.high_score = 0
        self.load()

    def load(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                self.high_score = data.get("high_score", 0)
        except:
            self.high_score = 0

    def save(self):
        with open(self.file, "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def update(self, score):
        if score > self.high_score:
            self.high_score = score
            self.save()