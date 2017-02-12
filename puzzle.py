from random import shuffle, randint, sample
from string import ascii_uppercase


commands = ["help","exit","rotate","find"]
bool_answers = ["yes","no"]
directions = ["right","left","up","down"]
messages = {"incorret_word":" is not on the list.", 
			"already_found_word":" was already found.",
			"good_word":"Congratulations! You just found ",
			"welcome":"WORD SEARCH PUZZLE\n\nLet's play!\n",
			"winner":" is the winner.",
			"win": "\n\n\nCongratulations! You found all the words. You won. ",
			"highscore": "NEW HIGHSCORE",
			"invalid_direction": "\nThat is an invalid direction. Only 'right', 'left', 'up', 'down' are possible.",
			"invalid_cell": "\nThat cell is not inside the board.",
			"invalid_row": "\nThat row is not inside the board.",
			"invalid_column": "\nThat column is not inside the board.",
			"invalid_number_spaces": "\nInvalid number of spaces.",
			"invalid_command": "\nThat is an invalid command. Only 'rotate', 'word', 'help', 'exit' are possible.\n",
			"it_is_not_a_line": "\nThose cells does not form a vertical or an horizontal line.",
			"it_is_not_an_integer": "\nIt must be an integer.",
			"insert_direction": "Direction ? ",
			"insert_number_spaces": "Spaces ? ",
			"insert_row_number": "Row number ?  ",
			"insert_column_number": "Column number ?  ",
			"menu": "MENU\n\n[p] Play\n[h] Help\n[e] Exit\n",
			"single_player_modes":"MODE\n\nPractice mode\n",
			"error": "\nAn error occurred. Leaving the game.\n",
			"exit_game": "\nLeaving the game.\n",
			"insert_command": "\nAction ? ",
			"play_again": "\n\nPlay again [yes/no] ? ",
			"words_to_find":"Words to find: ",
			"separator": "\n**************************************************\n"}

class Instruction:

	def __init__ (self):
		self.instruction = None

	def import_instruction(self, file):
		try: 
			f = open(file,'r')
			self.instruction = f.read()
		except:
			print(messages["error"])

	def display(self):
		print(self.instruction)

inst = Instruction()

def display_initial_message():
	print (messages["welcome"])

def display_menu():
	print (messages["menu"])

def display_single_player_modes():
	print (messages["single_player_modes"])

def get_player_nickname():
	pass


def setup():
	pass

def exit_game():
	print (messages["exit_game"])
	exit()
	


class Player:
# Version 1.0
	def __init__(self, nickname):
		self.nickname = nickname
		self.clue = None

	def set_clue(self, clue):
		''' Set a created clue into the player's clue. 

		Parameters:
		----------
			clue: BySolution(Clue)
				A clue object

		'''
		pass

class Board:
# Version 1.0

	def __init__(self):
		self.original_grid = [[]]
		self.current_grid = [[]]
		self.rows = 10
		self.columns = 10
		self.min_word_length = 3

	def build (self, words):
		''' Add to the board all the words given and fill the 
			blanks spaces left with random letters 

		Parameters:
		----------
			words: [string]
				An array with the words.

		'''
		self.current_grid = [['' for x in range(10)] for y in range(10)]
		num_words = len(words)
		words.sort(key=len)
		words.reverse()
		cols = [0,1,2,3,4,5,6,7,8,9]
		rows = [0,1,2,3,4,5,6,7,8,9]
		for word in words:
			added = False
			while not added:
				position = randint(0,1) # 0 is row, 1 is column.
				if position and len(cols) > 0:
					num = sample(cols,1)[0]
					added = self.add_word_into_row(num,word)
					if added:
						cols.remove(num)
				elif not position and len(rows) > 0:
					num = sample(rows,1)[0]
					added = self.add_word_into_column(num,word)
					if added:
						rows.remove(num)
		self.fill()

		# Copy the built list.
		self.original_grid = []
		for row in self.current_grid:
			self.original_grid.append(list(row))

	def restart_board(self):
	# Restart the board to its original state
		pass

	def is_valid_row(self,row):
		""" Check if the row number is inside the grid.
			
		Args: 
			row (int): row number.

		Returns:
			bool: True for success, False otherwise.

		"""
		if row < self.rows and row >= 0: 
			return True
		return False

	def is_valid_column(self,column):
		""" Check if the column number is inside the grid.
			
		Args: 
			column (int): column number.

		Returns:
			bool: True for success, False otherwise.

		"""
		if column < self.columns and column >= 0:
			return True
		return False

	def is_valid_number_spaces(self,direction,number):
		""" Check if the number is to rotate is correct.
			
		Args: 
			direction (str): direction to rotate.
			number (int): number of spaces to rotate.

		Returns:
			bool: True for success, False otherwise.

		"""
		if number > 0 and \
			(((direction == "up" or direction == "down") and \
				number < self.columns) or\
			((direction == "left" or direction == "right") and\
				number < self.rows)):
				return True
		return False

	def rotate_horizontally(self, row, number, direction):
		""" Rotates a row of the current grid a 'number' amount of spaces.
			
		Args: 
			row (int): row number to rotate.
			number (int): number of space to rotate.
			direction (str): "left" or "right"

		Return: 
			bool: True if the board was successfully rotate, False otherwise.

		"""
		if self.is_valid_row(row):
			number = number % self.rows
			if direction == "right":
				self.current_grid[row] = self.current_grid[row][-number:] +\
										 self.current_grid[row][:-number]
			elif direction == "left":	
				self.current_grid[row] = self.current_grid[row][number:] +\
										 self.current_grid[row][:number]
			return True
		return False
	
	def rotate_vertically(self, column, number, direction):
		""" Rotates a column of the current grid a 'number' amount of spaces.
			
		Args: 
			column (int): column number to rotate.
			number (int): number of space to rotate.
			direction (str): "up" or "down"

		Returns: 
			bool: True if the board was successfully rotate, False otherwise.
			
		"""
		if self.is_valid_column(column):
			number = number % self.columns
			temp_col=[]
			for i in range(self.columns):
				temp_col.append(self.current_grid[i][column])

			if direction == "up":
				temp_col = temp_col[number:] + temp_col[:number]
			elif direction == "down":
				temp_col = temp_col[-number:] + temp_col[:-number]
		
			for i in range(self.columns):
				self.current_grid[i][column]=temp_col[i]
			return True
		return False

	def get_letter(self,row,column):
		if self.is_valid_cell(row,column):
			return self.current_grid[row][column]
		return None

	def display(self):
		""" Display the grid on the standard output.	"""
		print ("\n   ", end='')
		for i in range (self.columns):
			print (str(i) + "   ", end='')
		print("\n")
		for i in range (self.rows):
			for j in range (self.columns):
				if j == 0:
					print (str(i) + "  ", end='')
				print (self.get_letter(i,j) + "   ", end='')
				if j == self.rows - 1:
					print (str(i), end='')
			print("\n")
		print ("   ", end='')
		for i in range (self.columns):
			print (str(i) + "   ", end='')
		print("\n")



	def is_valid_cell(self,row,column):
		""" Check if the cell is inside the grid.
			
		Args: 
			row (int): row number.
			column (int): column number.

		Returns:
			bool: True for success, False otherwise.

		"""
		if self.is_valid_row(row) and self.is_valid_column(column):
			return True
		return False


	def can_generate_a_word(self,row1,column1,row2,column2):
		''' Receive 2 cells and check they are valid, 
			if they form a vertical or an horizontal line,
			and if they form a word long enough.

		Args:
			row1 (int): row number of the starting cell.
			column1 (int): column number of the starting cell.
			row2 (int): row number of the final cell.
			column2 (int): column number of the final cell.

		Returns
			bool: True for success, False otherwise.

		'''
		if  (self.is_valid_cell(row1,column1) and 
			 self.is_valid_cell(row2,column2) and \
			
			(row1 == row2 and column1 != column2 and 
			 abs(column1 - column2) >= self.min_word_length) or \
			
			(column1 == column2 and row1 != row2 and \
			abs(row1 - row2) >= self.min_word_length)):
			return True
		return False


	def get_word(self,row1,column1,row2,column2):
		""" Get the word from the grid. The word is specified by a starting cell
			and a final cell.
		
		Args:
			row1 (int): row number of the starting cell.
			column1 (int): column number of the starting cell.
			row2 (int): row number of the final cell.
			column2 (int): column number of the final cell.

		Returns
			str: word obtained from the grid. None if the cells are not valid.

		"""

		if self.can_generate_a_word(row1,column1,row2,column2):
			word = "" 
			# The word is placed horizontally
			if (row1 == row2):
				start = min(column1,column2)
				end = max(column1,column2)
				for i in range (start,end+1):
					word = word + self.get_letter(row1,i)
				return word
			# The word is placed vertically
			elif (column1 == column2):
				start = min(row1,row2)
				end = max(row1,row2)
				for i in range (start,end+1):
					word = word + self.get_letter(i,column1)
				return word
		else:
			return None


	def add_word_into_row(self, row, word):
		''' Insert a word into a row of the board. 

		Parameters:
		----------
			row: integer
				The number of the row.
			word: string
				The word to be inserted.

		'''
		column = randint(0,9)
		aux_column = column
		# Checking the posibility to add the word
		for letter in word:
			if aux_column > 9:
				aux_column = 0
			if self.current_grid[row][aux_column] != '':
				if self.current_grid[row][aux_column] != letter:
					return False
			aux_column += 1
		# Adding the word.
		for letter in word:
			if column > 9:
				column = 0
			if self.current_grid[row][column] == '':
				self.current_grid[row][column] = letter
			column += 1
		return True

	def add_word_into_column(self, column, word):
		''' Insert a word into a column of the board. 

		Parameters:
		----------
			column: integer
				The number of the column.
			word: string
				The word to be inserted.

		'''
		row = randint(0,9)
		aux_row = row
		# Checking the posibility to add the word
		for letter in word:
			if aux_row > 9:
				aux_row = 0
			if self.current_grid[aux_row][column] != '':
				if self.current_grid[aux_row][column] != letter:
					return False
			aux_row += 1
		# Adding the word.
		for letter in word:
			if row > 9:
				row = 0
			if self.current_grid[row][column] == '':
				self.current_grid[row][column] = letter
			row += 1
		return True

	def fill(self):
		''' Fill the blak spaces with random letters.'''

		alfabet = ascii_uppercase
		for i in range(10):
			for j in range(10):
				if self.current_grid[i][j] == '':
					self.current_grid[i][j] = sample(alfabet,1)[0]


class Subject:
# Version 1.0

	def __init__(self, name):
		self.name = name
		self.content = []

	def add_word(self, word):
	#Add a word to self.content.
		pass

	def import_subject(self, file):
	# Import all the words corresponding to a subject from a file
		pass

	def get_name(self):
		''' Return the name of the subject. 

		Return:
		------
			string
				The name - Valid case.

		'''
		return self.name

	def get_words(self):
		''' Return all the words of the subject.

			Return:
			------
				[string]
					The words. Can be empty.

		'''
		return self.content


class Dictionary:
# Version 1.0
	def __init__(self):
		self.subjects = []

	def add_subject(self, subject):
	# Return if there was an error.
	# Version 1.0
		pass

	def display_subjects(self):
		''' Display the list of the names of the subjects. '''
		print('Subjects: ')
		for subject in self.subjects:
			print('- ' + subject.get_name())
		print('')

	def load(self,file):
	# Version 1.0
		pass

	def get_subject_by_name(self, name):
		''' Return a subject using its name element.

		Parameters:
		----------
			name: string
				The name of the subject as a string

		Return:
		------
			Subject
				Valid case.
			None 
				Invalid case. 

		'''
		for subject in self.subjects:
			if subject.get_name() == name:
				return subject
		return None

class Clue:
# Version 1.0

	def __init__(self):
		self.subject_name = None
		self.words_not_found = []
		self.words_found = []

	def build(self, subject, n):
		''' Build the clue, using the words of a subject, adding randomly
			the words into the not found list. In this version, there will 
			be 12 clues per board by default.

		Parameters:
		----------
			subject: Subject
				Subject object that contain the words to be used.
			n: integer
				Number of words to be selected.

		'''
		self.subject_name = subject.get_name()
		words = list(subject.get_words())
		# Functions from Python Random Lib.
		shuffle(words)
		if len(words) < n:
			lim = len(words)
		elif n <= 0:
			lim = 12
		else:
			lim = n
		for i in range(lim):
			self.add_word_to_not_found(words[i].upper())


	def already_found(self,word):
		""" Cheks if a word is on the list of words already found.

		Args:
			word (str): word to be checked.

		Returns:
			bool: True for success, False otherwise.

		"""
		return (word in self.words_found)

	def word_not_found(self,word):
		""" Cheks if a word is on the list of words that have not been found.

		Args:
			word (str): word to be checked.

		Returns:
			bool: True for success, False otherwise.
			
		"""
		return (word in self.words_not_found)

	def word_in_clue(self, word):
		""" Cheks if a word belongs to a clue. Checks if a word is included on
			the list of words already found or on the list of words that have 
			not been found.

		Args:
			word (str): word to be checked.

		Returns:
			bool: True for success, False otherwise.
			
		"""		
		return (self.already_found(word) or self.word_not_found(word))

	def add_word_to_not_found(self, word):
		''' Add a word to the clue as not found.

		Parameters:
		----------
			word: string
				Word that will be added.

		'''
		if word == "" or word == None:
			print("Error: Incorrect format. It was not added.")
		else:
			self.words_not_found.append(word)

	def add_word_to_found(self, word):
		""" Add a word to the list of words that have been found.

		Args:
			word (str): word to be added.

		"""		
		self.words_found.append(word)

	def remove_word_from_not_found(self, word):
		""" Check if the word is on the list of words that have not been found
			and removed it.

		Args:
			word (str): word to be removed.

		Returns: 
			bool: True if the word was successfully removed. False otherwise.

		"""	
		if (self.word_not_found(word)):
			self.words_not_found.remove(word)
			return True
		return False

	def found_all_the_words(self):
		""" Check if the list of words that have not been found is empty and
			the list of words that have been found is not empty.

		Returns: 
			bool: True for success, False otherwise.

		"""	
		return ((len(self.words_not_found) == 0) and\
				(len(self.words_found) != 0))

	def get_words_not_found(self):
		''' Return the list of words not found. 

		Parameters:
		----------
			[string]
				Words not found.

		'''
		return self.words_not_found


class BySubject(Clue):

	def display (self):
		pass

class BySolution(Clue):
# Version 1.0

	def display (self):
	# Version 1.0
		print(messages["words_to_find"])
		print(self.words_not_found)
		
class ByLetters(Clue):

	def display (self):
		pass
		
class ByLength(Clue):

	def display (self):
		pass


class Score:
	# IS THE NICK NAME ENOUGH?
	def __init__ (self, nickname, points):
		self.nickname = nickname
		self.points = points

	def __str__(self):
		pass

class HighScores:

	# SEPARATE AS 2 INTANCES?

	def __init__(self):
		self.simple_mode = []
		self.racetime_mode = []

	def add_simple_mode_highscore(self, score):
		pass
	
	def add_race_time_mode_highscore(self, score):
		pass

	def import_highscores(self, file):
		pass
		
	def export_highscores(self, file):
		pass

	def is_highscore(self, score):
		pass

	def display(self):
		pass


class Game:
# Version 1.0

	def __init__(self):
		self.board = None
		self.clue = None
		self.start_again = False

	def add_board(self, board):
		''' Add the board into the element board of the game 

		Parameters:
		----------
			board: Board
				Object of type Class Board.

		'''
		self.board = board
		

	def select_subject(self):
		''' Return a selected subject from the dictionary.

		Return:
		------
		Subject
			the selected subject - Valid case.

		'''
		sname = ""
		subject = None
		while subject == None:
			print('Please, choose a correct subject...')
			dictionary.display_subjects()
			sname = input("Type here your subject: ")
			subject = dictionary.get_subject_by_name(sname)
			if subject == None:
				print('----------------------------------------------')
				print('Error: It is not a correct subject. Try again.')
		return subject

	def select_clue(self, subject):
		''' Select an specific type of clue. For this version,
			it will be BySolution.

		Parameters:
		----------
			subject: Subject
				subject that will be used into the building clue processes.

		'''
		clue = BySolution()
		if subject == None:
			print("Error: Incorrect format. It was not selected")
		else:
			clue.build(subject,12)
			self.clue = clue


	def get_row_number(self):
		""" Read from standard input an integer.

		Returns: 
			int: row number read. 

		"""	
		is_valid = False
		while not is_valid:
			try: 
				n = int(input(messages["insert_row_number"]))
				if self.board.is_valid_row(n):
					return n
				print(messages["invalid_row"])
			except:
				print(messages["it_is_not_an_integer"])

	def get_column_number(self):
		""" Read from standard input an integer.

		Returns: 
			int: column number read. 

		"""	
		is_valid = False
		while not is_valid:
			try:
				n = int(input(messages["insert_column_number"]))
				if self.board.is_valid_column(n):
					return n
				print(messages["invalid_column"])
			except:
				print(messages["it_is_not_an_integer"])

	def find_word(self):
		""" Find a word specified by the user. Get the row and the column 
			numbers corresponding to initial and the final cells of the word.
			Get the word from the board, and check if the word is valid.
			Display appropiate messages to the user.

		"""	
		row1 = self.get_row_number()
		column1 = self.get_column_number()
		row2 = self.get_row_number()
		column2 = self.get_column_number()
		word = self.board.get_word(row1,column1,row2,column2)
		if word != None:
			if not self.clue.word_in_clue(word):
				print("'" + word + "'"+ messages["incorret_word"])
				return
			if self.clue.already_found(word):
				print(messages["already_found_word"]+ "'" + word + "'.")
			else:
				self.clue.add_word_to_found(word)
				self.clue.remove_word_from_not_found(word)
				print(messages["good_word"] + "'" + word + "'.")
		else:
			print(messages["it_is_not_a_line"])

	def setup(self):
		''' Setup all the configuration of the game before starting.'''

		selected_subject = self.select_subject()
		self.select_clue(selected_subject)
		words = list(self.clue.get_words_not_found())
		new_board = Board()
		new_board.build(words)
		self.add_board(new_board)

	def get_direction(self):
		""" Read from standard input a string corresponding to a direction.
		Only 'right', 'left', 'up', 'down' are possible.
		
		Returns: 
			str: direction read. 

		"""	
		is_valid = False
		while not is_valid:
			direction = (input(messages["insert_direction"])).lower()
			if direction in directions:
				return direction
			print(messages["invalid_direction"])

	def get_number_spaces(self,direction):
		""" Read from standard input an integer.
		
		Arguments:
			direction (str): direction the board is going to rotate.

		Returns: 
			int: number of spaces read. 

		"""	
		is_valid = False
		while not is_valid:
			try:
				n = int(input(messages["insert_number_spaces"]))
				if self.board.is_valid_number_spaces(direction,n):
					return n
				print(messages["invalid_number_spaces"])
			except:
				print(messages["it_is_not_an_integer"])


	def get_rotation_attr(self): 
		""" Get the direction to rotate the board, the number of row or column
		that is going to rotate and the amount of spaces to rotate. Then
		rotates the board accordint to these parameters.

		"""	
		direction = self.get_direction()
		if direction == "up" or direction == "down":
			row = self.get_column_number()
			number = self.get_number_spaces(direction)
			self.board.rotate_vertically(row,number,direction)
		elif direction == "left" or direction == "right":
			column = self.get_row_number()
			number = self.get_number_spaces(direction)
			self.board.rotate_horizontally(column,number,direction)

	def get_play_again(self):
		''' Ask the user if he-she wants to start a new game.

		Returns:
			bool = True if success, False otherwise.
		'''
		while True:
			answer = (input(messages["play_again"])).lower()
			if answer in bool_answers:
				if answer == "yes":
					return True
				elif answer == "no":
					return False

	def end_current_game(self):

		if self.get_play_again():
			self.start_again = True
		else:
			exit_game()

	def read_command(self):
		'''' Reads a command from standard input. Only 'rotate', 'word', 'help', 
		'exit' are valid. Calls the corresponding function to execute each command.

		'''
		is_valid = False
		while not is_valid:
			command = (input(messages["insert_command"])).lower()
			if command in commands:
				if command == "help":
					inst.display()
				elif command == "exit":
					self.end_current_game()	
				elif command == "rotate":
					self.get_rotation_attr()
				elif command == "find":
					self.find_word()
				return None
			else:
				print(messages["invalid_command"])

	def turn(self):
		''' Manages the turns of the player. Call the function to read the
			commands, and display the current state of the game. 

		'''
		print (messages["separator"])
		self.board.display()
		self.clue.display()
		self.read_command()


class SinglePlayer(Game):
# Version 1.0

	def __init__(self):
		self.player = None
<<<<<<< HEAD
=======

	def add_player(self,player):
		pass
>>>>>>> turns

	def display_current_state(self):
	# Display the board, the list of words according to the clue
	# Version 1.0
		pass

	def restart(self):
	# Version 1.0
		pass


class PracticeMode(SinglePlayer):
# Version 1.0

	def is_win (self):
		return (self.clue.found_all_the_words())

	def play(self):
	# Version 1.0
		self.start_again = False
		while not self.start_again:
			self.turn()
			if self.is_win():
				print(messages["win"])
				self.end_current_game()
		
	def restart(self):
	# Version 1.0
		pass
		
class SimpleMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 0
		
	def play(self):
		pass
		
	def manage_time(self):
	# Starts the time
	# Thread 
		pass

	def compute_score(self, words, time):
		pass


class TimeRaceMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 0
		self.final_time = 0

	def manage_time(self):
	# Takes the time
		pass

	def is_time_over(self):
		pass
	
	def play(self):
		pass

	def compute_score(self, words, time):
		pass

class MultiPlayer(Game):

	def __init__ (self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1
		self.time_per_turn = 0

	def display_current_state(self):
	# Display the board, the list of words according to the clue
	# The name of the player in turn
		pass

	def set_current_player(self):
	# change of current_player
		pass

	def manage_time(self):
	# take the time corresponding to each turn
		pass

	def play(self):
		pass

	def is_time_over(self):
		pass

	def display_winner(self):
		pass

	def restart(self):
	# Setup of the game again, keeping the same players.
		pass

def start_game():
	
	game = PracticeMode()
	# Asign board
	# Asign clue
	game.play()

<<<<<<< HEAD
# Dictionary of words.
dictionary = Dictionary()
=======
def configure_instructions():
	inst.import_instruction("instructions.txt")
	
>>>>>>> turns

def main():

	configure_instructions()

if __name__ == '__main__':
  main()


	
