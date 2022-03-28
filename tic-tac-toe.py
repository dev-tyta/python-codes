import random

ticBoard = {'top_L': " ", 'top_M': " ", 'top_R': " ",
            'mid_L': " ", 'mid_M': " ", 'mid_R': " ",
            'low_L': ' ', 'low_M': ' ', 'low_R': ' '}

wins_X = 0
wins_O = 0


def print_board(board):
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print("-+-+-")
    print(board["mid_L"] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print("-+-+-")
    print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])


def score_board():
    print("Score Board@@")
    print(f"X : {wins_X}  |  O: {wins_O}")


print("How many Games would you love to play....")
game = input()
turn = random.choice(["X", "O"])
for i in range(9):
    print_board(ticBoard)
    print(f"Turn for {turn}. You are allowed to pick a space to move to."
          f"They are top_L(Top Left Corner), top_M(Top Middle Space), top_R(Top Right Corner)"
          f"mid_L (Middle Left Space), mid_M(Middle Space), mid_R(Middle Right Space)"
          f"low_L(Bottom Left Corner), low_M(Bottom Middle Space), low_R(Bottom Right Corner) ")
    move = input("MOve to which space: ")
    ticBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    if ticBoard["top_L"] == ticBoard["top_M"] == ticBoard["top_R"] != " ":
        winner = ticBoard["top_L"]
        break
    elif ticBoard["mid_L"] == ticBoard["mid_M"] == ticBoard["mid_R"] != " ":
        winner = ticBoard["mid_L"]
        break
    elif ticBoard["low_L"] == ticBoard["low_M"] == ticBoard["low_R"] != " ":
        winner = ticBoard["low_L"]
        break
    else:
        print("No winner!! Replay")

print_board(ticBoard)
print(f"{winner} Wins this round")
