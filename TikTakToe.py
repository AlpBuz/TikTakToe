import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game board
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
currentPlayer = "X"

def buttonClick(row, col):
    global currentPlayer

    if board[row][col] == " ":
        board[row][col] = currentPlayer
        buttons[row][col].config(text=currentPlayer)

        if checkWinner(board):
            messagebox.showinfo("Game Over", f"Player {currentPlayer} has won!")
            resetBoard()
        elif checkDraw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            resetBoard()
        else:
            currentPlayer = "O" if currentPlayer == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This spot is already taken!")

def checkWinner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def resetBoard():
    global currentPlayer, board

    currentPlayer = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=" ", font='Helvetica 20 bold', height=3, width=6,
                           command=lambda row=row, col=col: buttonClick(row, col))
        button.grid(row=row, column=col)
        buttons[row][col] = button

root.mainloop()
