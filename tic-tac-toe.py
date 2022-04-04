import random  # importing libraries

ticBoard = {'top_L': " ", 'top_M': " ", 'top_R': " ",
            'mid_L': " ", 'mid_M': " ", 'mid_R': " ",
            'low_L': ' ', 'low_M': ' ', 'low_R': ' '}  # represents tic-tac-toe table

wins_X = 0  # default point for X
wins_O = 0  # default point for O


def print_board(board):  # prints selected board out
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print("-+-+-")
    print(board["mid_L"] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print("-+-+-")
    print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'] + "\n")


def score_board():  # records score during game.
    print("Score Board")
    print(f"X : {wins_X}  |  O: {wins_O}")


print("Multiplayer or Single PLayer:(If Multiplayer input M, else input S for SinglePlayer.)")
player_choice = input().upper()  # gets input to know if player would play multiplayer or single-player.
print("How many Games would you love to play....")
game_turns = int(input())  # collects number of game player(s) would love to play.
try:
    for i in range(game_turns):  # carries out a loop depending on the number of times players would like to play.
        score_board()
        if player_choice == "M":  # if a player decides to play a multiplayer game.
            turn = random.choice(["X", "O"])  # automatically selects a key for players
            post = list(ticBoard.keys())  # available positions.
            for num in range(9):  # carries out loop till someone wins.
                print_board(ticBoard)
                print(f"""Turn for {turn}. You are allowed to pick a space to move to.
                     They are top_L(Top Left Corner), top_M(Top Middle Space), top_R(Top Right Corner)
                     mid_L (Middle Left Space), mid_M(Middle Space), mid_R(Middle Right Space)
                     low_L(Bottom Left Corner), low_M(Bottom Middle Space), low_R(Bottom Right Corner) """)
                print(f"Available Positions are {post} ")  # prints out the available position where players can play.
                move = input("Move to which space: ")  # collects an input of position where players would love to play
                ticBoard[move] = turn  # assigns players key to the position chosen
                post.remove(move)  # removes the position that has been used.
                if turn == "X":  # alternates to next player
                    turn = "O"
                else:
                    turn = "X"
        elif player_choice == "S":  # if player which to play a single player game.
            turn = "X"  # player is automatically assigned X
            post = list(ticBoard.keys())  # same as shown above
            for num in range(4):  # carries out loop 4 times since the player is playing against an automatic computer
                print_board(ticBoard)
                print(f"""Turn for {turn}. You are allowed to pick a space to move to.
                         They are top_L(Top Left Corner), top_M(Top Middle Space), top_R(Top Right Corner)
                         mid_L (Middle Left Space), mid_M(Middle Space), mid_R(Middle Right Space)
                         low_L(Bottom Left Corner), low_M(Bottom Middle Space), low_R(Bottom Right Corner) """)
                print(f"Available Positions are {post} ")
                move = input("Move to which space: ")
                ticBoard[move] = turn
                post.remove(move)
                if turn == "X":
                    comp_turn = "O"  # assigns computer a key
                else:
                    comp_turn = "X"
                comp_post = random.choice(post)  # allows the computer randomly picks a position.
                post.remove(comp_post)
                ticBoard[comp_post] = comp_turn  # computer key is assigned to the selected position
                print_board(ticBoard)

                # Laws that determines the winner.
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

        if winner == "X":  # if winner is X, a point is added to point won.
            wins_X += 1
        elif winner == "O":  # if winner is O, a point is added to point won.
            wins_O += 1
        else:  # in the case of a draw, no point is added
            wins_O = 0
            wins_X = 0

        print_board(ticBoard)
        if wins_O or wins_X >= 1:
            print(f"{winner} Wins this round")
        else:
            print("There is a tie....")
        score_board()
        ticBoard = {'top_L': " ", 'top_M': " ", 'top_R': " ",
                    'mid_L': " ", 'mid_M': " ", 'mid_R': " ",
                    'low_L': ' ', 'low_M': ' ', 'low_R': ' '}  # assigns an empty board for a new game.
    if wins_X > wins_O:  # shows final winner of the game or if it ends up in a tie.
        print(f"X wins with {wins_X} points")
    elif wins_O > wins_X:
        print(f"O wins with {wins_O} points")
    elif wins_O == wins_X:
        print("The Game ended a Draw...")
    else:
        print("Unknown possibility")

except ValueError:  # returns error when a number is not written.
    print("Input A number")
