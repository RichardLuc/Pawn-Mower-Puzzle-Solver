import copy

def print_board(board):
	for i in range(0, 8):
		print (8 - i, end = " ")
		for j in range(0,8):
			print (board[i][j], end = "|")
		print ("") #new line
	print ("", end = "  a|b|c|d|e|f|g|h")
	print ("")
	return None

def move_piece(board, piece, dir):
	newBoard = copy.deepcopy(board)
	for i in range(0, 8):
		for j in range(0, 8):
			if board[i][j] == piece:
				newBoard[i][j] = ' '
				break
		else:
			continue
		break

	if piece == 'r':
		if dir == 1:
			for x in range(i, -1, -1):
				if newBoard[x][j] == 'p':
					newBoard[x][j] = piece
					xCoord = 8 - x
					yCoord = j + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 2:
			for y in range(j, 8):
				if newBoard[i][y] == 'p':
					newBoard[i][y] = piece
					xCoord = 8 - i
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 3:
			for x in range(i, 8):
				if newBoard[x][j] == 'p':
					newBoard[x][j] = piece
					xCoord = 8 - x
					yCoord = j + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 4:
			for y in range(j, -1, -1):
				if newBoard[i][y] == 'p':
					newBoard[i][y] = piece
					xCoord = 8 - i
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
	elif piece == 'b':
		if dir == 1:
			for x, y in zip(range(i, -1, -1), range(j, 8)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 2:
			for x, y in zip(range(i, 8), range(j, 8)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 3:
			for x, y in zip(range(i, 8), range(j, -1, -1)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 4:
			for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
	elif piece == 'q':
		if dir == 1:
			for x in range(i, -1, -1):
				if newBoard[x][j] == 'p':
					newBoard[x][j] = piece
					xCoord = 8 - x
					yCoord = j + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 2:
			for x, y in zip(range(i, -1, -1), range(j, 8)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 3:
			for y in range(j, 8):
				if newBoard[i][y] == 'p':
					newBoard[i][y] = piece
					xCoord = 8 - i
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 4:
			for x, y in zip(range(i, 8), range(j, 8)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 5:
			for x in range(i, 8):
				if newBoard[x][j] == 'p':
					newBoard[x][j] = piece
					xCoord = 8 - x
					yCoord = j + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 6:
			for x, y in zip(range(i, 8), range(j, -1, -1)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 7:
			for y in range(j, -1, -1):
				if newBoard[i][y] == 'p':
					newBoard[i][y] = piece
					xCoord = 8 - i
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 8:
			for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
				if newBoard[x][y] == 'p':
					newBoard[x][y] = piece
					xCoord = 8 - x
					yCoord = y + 97
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
	elif piece == 'k':
		if dir == 1:
			if (i - 2) > -1 and (j + 1) < 8:
				if newBoard[i - 2][j + 1] == 'p':
					newBoard[i - 2][j + 1] = piece
					xCoord = 8 - i + 2
					yCoord = 97 + j + 1
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 2:
			if (i - 1) > -1 and (j + 2) < 8:
				if newBoard[i - 1][j + 2] == 'p':
					newBoard[i - 1][j + 2] = piece
					xCoord = 8 - i + 1
					yCoord = 97 + j + 2
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 3:
			if (i + 1) < 8 and (j + 2) < 8:
				if newBoard[i + 1][j + 2] == 'p':
					newBoard[i + 1][j + 2] = piece
					xCoord = 8 - i - 1
					yCoord = 97 + j + 2
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 4:
			if (i + 2) < 8 and (j + 1) < 8:
				if newBoard[i + 2][j + 1] == 'p':
					newBoard[i + 2][j + 1] = piece
					xCoord = 8 - i - 2
					yCoord = 97 + j + 1
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 5:
			if (i + 2) < 8 and (j - 1) > -1:
				if newBoard[i + 2][j - 1] == 'p':
					newBoard[i + 2][j - 1] = piece
					xCoord = 8 - i - 2
					yCoord = 97 + j - 1
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 6:
			if (i + 1) < 8 and (j - 2) > -1:
				if newBoard[i + 1][j - 2] == 'p':
					newBoard[i + 1][j - 2] = piece
					xCoord = 8 - i - 1
					yCoord = 97 + j - 2
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 7:
			if (i - 1) > -1 and (j - 2) > -1:
				if newBoard[i - 1][j - 2] == 'p':
					newBoard[i - 1][j - 2] = piece
					xCoord = 8 - i + 1
					yCoord = 97 + j - 2
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
		elif dir == 8:
			if (i - 2) > -1 and (j - 1) > -1:
				if newBoard[i - 2][j - 1] == 'p':
					newBoard[i - 2][j - 1] = piece
					xCoord = 8 - i + 2
					yCoord = 97 + j - 1
					nextSol = str(chr(yCoord)) + str(xCoord) 
					return newBoard, nextSol
			return False, False
	return False, False

def puzzle(board, piece, numDir, numPawns):
	boardList = []
	boardList.append(board)
	dirList = []
	firstDirList = [False] * numDir
	dirList.append(firstDirList)
	solution = []
	dir = 1
	pawns = numPawns
	bool = True

	while bool:
		currBoard = boardList[-1]
		nextBoard, nextSol = move_piece(currBoard, piece, dir)

		if nextBoard != False and dirList[-1][dir - 1] != True:
			boardList.append(nextBoard)
			solution.append(nextSol)
			dirList.append([False] * numDir)
			pawns -= 1
		else:
			dirList[-1][dir - 1] = True
			if dirList[-1] == [True] * numDir:
				del boardList[-1]
				del solution[-1]
				del dirList[-1]
				dir += 1
				if dir > numDir:
					dir = 1
				dirList[-1][dir - 1] = True
				pawns += 1
			else:
				dir += 1
				if dir > numDir:
					dir = 1
		if pawns == 0:
			bool = False

	print(solution)
	return None

def main():
	board = [[' ' for x in range(0, 8)] for y in range(0, 8)]

	#xCoord and yCoord takes in letters and numbers like an actual chess board
	#board takes in the coordinates in coloum major to put the pawns in the
	#correct spot
	numPawns = int(input("Enter the the amount of pawns on the board: "))
	for i in range(0, numPawns):
		xCoord = ord(input("Enter the x-coordinate of the pawn: "))
		xCoord = xCoord - 97
		yCoord = int(input("Enter the y-coordinate of the pawn: "))
		yCoord = 8 - yCoord
		board[yCoord][xCoord] = 'p'
		print(xCoord)
		print(yCoord)
	print("Here is what your board currently looks like:")
	print_board(board)

	piece = input("Enter the piece to control (rook, bishop, queen, knight):")
	xCoord = ord(input("Enter the x-coordinate of the " + piece + ": "))
	xCoord = 97 - xCoord
	yCoord = int(input("Enter the y-coordinate of the " + piece + ": "))
	yCoord = 8 - yCoord
	if piece == "rook":
		piece = 'r'
		numDir = 4
	elif piece == "bishop":
		piece = 'b'
		numDir = 4
	elif piece == "queen":
		piece = 'q'
		numDir = 8
	elif piece == "knight":
		piece = 'k'
		numDir = 8
	board[yCoord][xCoord] = piece

	puzzle(board, piece, numDir, numPawns)
	return None