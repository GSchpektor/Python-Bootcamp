# print game banner
# player_input(player) - ask for row and column, check if that position is taken
# display_board(), 7 rows of list
# build each row as a list to be able to replace " " with x or o
# function check_win()
#  play() 

board = [
	["", "", ""],
	["", "", ""],
	["", "", ""]
]

def is_valid(row, column):
	if board[row][column] == "":
		return True
	return False



def player_input(row, column, player):
	if 0 <= row <= 2:
		if is_valid(row, column):
			board[row][column] = player 
		else: 
			print("invalid move")
	else: 
		print("invalid number")



def display(board):
	print("*"*15)
	print("*", board[0][0], "|", board[0][1], "|", board[0][2], "*")
	print("*- - -", "|", "- - -", "|", "- - -	*")
	print("*", board[1][0], "|", board[1][1], "|", board[2][2], "*")
	print("*- - -", "|", "- - -", "|", "- - -	*")
	print("*", board[2][0], "|", board[2][1], "|", board[2][2], "*")
	print("*- - -", "|", "- - -", "|", "- - -*")
	print("*"*15)



def check_rows():
	for row in board:
		if row.count("X") == 3:
			return "X"
		if row.count("O") == 3:
			return "O"
	return None		

def check_columns():
	if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
		return "X"
	if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
		return "X"
	if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
		return "X"
	if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
		return "O"
	if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
		return "O"
	if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
		return "O"
	return None


def check_diagonals():
	if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
		return "X"
	if board[2][2] == "X" and board[1][1] == "X" and board[0][0] == "X":
		return "X"
	if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
		return "O"
	if board[2][2] == "O" and board[1][1] == "O" and board[0][0] == "O":
		return "O"
	return None

def move_available():
	for row in board:
		if "" in row:
			return True
	return False
	

def game_over(): ### 3 in one row, same index in each row, 123 or 321 index
	result = check_rows()
	if result != None:
		return result
	result = check_columns()
	if check_columns() != None:
		return result
	result = check_diagonals()
	if check_diagonals() != None:
		return result
	if not move_available():
		return "draw"
	return None




def play():
	player = "X"
	while True:
		result = game_over()
		if result != None:
			break
		
		player_row = int(input(f"Player {player}, select a row (1,2,3)"))-1
		player_column = int(input(f"Player {player}, select a column (1,2,3)"))-1
		player_input(player_row, player_column, player)

		player = "X" if player == "O" else "O"	


		display(board)
	if result == "draw":
		print(f"It's a draw")
	else:
		print(f"The winner is {result}")







