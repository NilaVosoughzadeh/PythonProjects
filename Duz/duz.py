# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("بازی دوز")
root.resizable(False, False)

current_player = "X"
board = [""] * 9
buttons = []

def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return "" not in board

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")
    status_label.config(text="نوبت بازیکن X")

def on_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(text=current_player)

    if check_winner(current_player):
        messagebox.showinfo("پایان بازی", f"بازیکن {current_player} برنده شد 🎉")
        disable_buttons()
        return

    if is_draw():
        messagebox.showinfo("پایان بازی", "بازی مساوی شد 🤝")
        disable_buttons()
        return

    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"نوبت بازیکن {current_player}")

# رابط گرافیکی
status_label = tk.Label(
    root,
    text="نوبت بازیکن X",
    font=("Tahoma", 14)
)
status_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Tahoma", 24),
        width=4,
        height=2,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

reset_button = tk.Button(
    root,
    text="شروع مجدد",
    font=("Tahoma", 12),
    command=reset_game
)
reset_button.pack(pady=10)

root.mainloop()