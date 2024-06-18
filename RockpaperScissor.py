import tkinter as tk
import random

# Initialize Tkinter
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'


# Function to handle user's choice
def user_choice(choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    winner = determine_winner(choice, computer_choice)

    user_label.config(text=f"You chose: {choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if winner == 'tie':
        result_label.config(text="It's a tie!")
    elif winner == 'user':
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")


# GUI elements
choices = ['rock', 'paper', 'scissors']

user_label = tk.Label(root, text="Make your choice:")
user_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    button = tk.Button(button_frame, text=choice.capitalize(),
                       width=10,
                       command=lambda ch=choice: user_choice(ch))
    button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

computer_label = tk.Label(root, text="")
computer_label.pack()

# Start the main Tkinter event loop
root.mainloop()
