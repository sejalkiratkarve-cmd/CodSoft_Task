import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    
    user_label.config(text="You chose: " + user_choice)
    comp_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)

    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="")
    comp_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Score - You: 0  Computer: 0")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")

tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)


user_label = tk.Label(root, text="", font=("Arial", 12))
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 12))
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)


tk.Button(root, text="Play Again / Reset", command=reset_game).pack(pady=10)

root.mainloop()