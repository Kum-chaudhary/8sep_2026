
import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
SPEED = 120

class SnakeGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Python Snake Game")
        self.root.resizable(False, False)

        # Score
        self.score = 0
        self.game_over = False
        self.after_id = None

        # Score label
        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 18, "bold")
        )
        self.score_label.pack(pady=10)

        # Game canvas
        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg="black"
        )
        self.canvas.pack()

        # Restart button
        self.restart_btn = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 12),
            command=self.restart_game
        )
        self.restart_btn.pack(pady=10)

        # Keyboard controls
        self.root.bind("<Up>", lambda e: self.change_direction("Up"))
        self.root.bind("<Down>", lambda e: self.change_direction("Down"))
        self.root.bind("<Left>", lambda e: self.change_direction("Left"))
        self.root.bind("<Right>", lambda e: self.change_direction("Right"))

        self.restart_game()

    # Start or restart game
    def restart_game(self):

        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.score = 0
        self.game_over = False

        # Snake body positions
        self.snake = [
            (100, 100),
            (80, 100),
            (60, 100)
        ]

        # Initial direction
        self.direction = "Right"

        # Previous direction
        self.previous_direction = "Right"

        self.score_label.config(text="Score: 0")

        self.food = self.create_food()

        self.draw_game()
        self.move_snake()

    # Create food randomly
    def create_food(self):

        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)

            position = (x, y)

            if position not in self.snake:
                return position

    # Change snake direction
    def change_direction(self, new_direction):

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        if new_direction != opposite[self.previous_direction]:
            self.direction = new_direction

    # Move snake
    def move_snake(self):

        if self.game_over:
            return

        x, y = self.snake[0]

        if self.direction == "Up":
            y -= CELL_SIZE

        elif self.direction == "Down":
            y += CELL_SIZE

        elif self.direction == "Left":
            x -= CELL_SIZE

        elif self.direction == "Right":
            x += CELL_SIZE

        new_head = (x, y)

        # Check wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            self.end_game()
            return

        # Check food
        eating_food = new_head == self.food

        # Check body collision
        body_to_check = self.snake if eating_food else self.snake[:-1]

        if new_head in body_to_check:
            self.end_game()
            return

        # Add new head
        self.snake.insert(0, new_head)

        if eating_food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.create_food()

        else:
            self.snake.pop()

        self.previous_direction = self.direction

        self.draw_game()

        # Repeat movement
        self.after_id = self.root.after(SPEED, self.move_snake)

    # Draw snake and food
    def draw_game(self):

        self.canvas.delete("all")

        # Draw snake
        for x, y in self.snake:

            self.canvas.create_rectangle(
                x, y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill="lime",
                outline="black"
            )

        # Draw food
        x, y = self.food

        self.canvas.create_oval(
            x, y,
            x + CELL_SIZE,
            y + CELL_SIZE,
            fill="red",
            outline="white"
        )

    # Game over
    def end_game(self):

        self.game_over = True

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text="GAME OVER!",
            fill="white",
            font=("Arial", 30, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 45,
            text=f"Final Score: {self.score}",
            fill="yellow",
            font=("Arial", 18)
        )


# Main program
root = tk.Tk()

game = SnakeGame(root)

root.mainloop()
