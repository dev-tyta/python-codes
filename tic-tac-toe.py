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
    print("Score Board")
    print(f"X : {wins_X}  |  O: {wins_O}")


print("Multiplayer or Single PLayer:(If Multiplayer input M, else input S for SinglePlayer.)")
player_choice = input()
print("How many Games would you love to play....")
game_turns = int(input())
try:
    for i in range(game_turns):
        score_board()
        if player_choice == "M":
            turn = random.choice(["X", "O"])
            for num in range(9):
                print_board(ticBoard)
                print(f"""Turn for {turn}. You are allowed to pick a space to move to.
                     They are top_L(Top Left Corner), top_M(Top Middle Space), top_R(Top Right Corner)
                     mid_L (Middle Left Space), mid_M(Middle Space), mid_R(Middle Right Space)
                     low_L(Bottom Left Corner), low_M(Bottom Middle Space), low_R(Bottom Right Corner) """)
                move = input("Move to which space: ")
                ticBoard[move] = turn
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
        elif player_choice == "S":
            turn = random.choice(["X", "O"])
            for num in range(4):
                print_board(ticBoard)
                print(f"""Turn for {turn}. You are allowed to pick a space to move to.
                         They are top_L(Top Left Corner), top_M(Top Middle Space), top_R(Top Right Corner)
                         mid_L (Middle Left Space), mid_M(Middle Space), mid_R(Middle Right Space)
                         low_L(Bottom Left Corner), low_M(Bottom Middle Space), low_R(Bottom Right Corner) """)
                move = input("Move to which space: ")
                ticBoard[move] = turn
                post = list(ticBoard.keys())
                post.remove(move)
                if turn == "X":
                    comp_turn = "O"
                else:
                    comp_turn = "X"
                comp_post = random.choice(post)
                post.remove(comp_post)
                ticBoard[comp_post] = comp_turn
                print_bo

                if ticBoard["top_L"] == ticBoard["top_M"] == ticBoard["top_R"] != " ":
                    winner = ticBoard["top_L"]
                    break
                elif ticBoard["mid_L"] == ticBoard["mid_M"] == ticBoard["mid_R"] != " ":
                    winner = ticBoard["mid_L"]
                    break
                elif ticBoard["low_L"] == ticBoard["low_M"] == ticBoard["low_R"] != " ":
                    winner = ticBoard["low_L"]
                    break
                elif ticBoard["top_L"] == ticBoard["mid_L"] == ticBoard["low_L"] != " ":
                    winner = ticBoard["top_L"]
                    break
                elif ticBoard["top_M"] == ticBoard["mid_M"] == ticBoard["low_M"] != " ":
                    winner = ticBoard["top_M"]
                    break
                elif ticBoard["low_R"] == ticBoard["top_R"] == ticBoard["mid_R"] != " ":
                    winner = ticBoard["top_R"]
                    break
                elif ticBoard["top_L"] == ticBoard["mid_M"] == ticBoard["low_R"] != " ":
                    winner = ticBoard["top_L"]
                    break
                elif ticBoard["low_L"] == ticBoard["mid_M"] == ticBoard["top_R"] != " ":
                    winner = ticBoard["top_L"]
                    break

            if winner == "X":
                wins_X += 1
            elif winner == "O":
                wins_O += 1
            else:
                wins_O = 0
                wins_X = 0

        print_board(ticBoard)
        print(f"{winner} Wins this round")
        score_board()
        ticBoard = {'top_L': " ", 'top_M': " ", 'top_R': " ",
                    'mid_L': " ", 'mid_M': " ", 'mid_R': " ",
                    'low_L': ' ', 'low_M': ' ', 'low_R': ' '}

except ValueError:
    print("Input A number")
