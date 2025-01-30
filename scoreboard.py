from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
DATA_FILE = "data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()  # Load high score from file
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update scoreboard display with the current score and high score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset current score and update high score if a new record is set."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()  # Save new high score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase score and update scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def save_high_score(self):
        """Save the high score to a text file."""
        with open(DATA_FILE, "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        """Load the high score from a text file. Create a new file if missing."""
        try:
            with open(DATA_FILE, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0  # If file doesn't exist, return 0
