"""
File: boggle.py
Name: Angel Chen
----------------------------------------
The aim is to create a Python program that plays Boggle.
The words must be made up of neighboring squares, and you can't use the same square twice in a word.
Words don't need to be in a straight line.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dict_list = []     # A list that contains the words with more than four letters in the dictionary
found_words = []   # A list that contains all of the words we found


def main():
	"""
	Given a 4x4 board, this Python program prints out all of the words contained within the board.
	"""
	read_dictionary()
	print('Welcome to stanCode \"Boggle Game\" (Please input 4 rows of letters.)')

	# Create an empty Boggle board, with a given word list input by user
	input_data = []
	for i in range(1, 5):
		letter = input(f"{i} row of letters: ").lower()
		if not test_input(letter):
			break
		strip_letter = letter.strip().split()
		input_data.append(strip_letter)

	play_boggle(input_data)
	print(f'There are {len(found_words)} words in total.')


def play_boggle(input_data):
	"""
	Finds all adjacent words hidden in a grid of letters on the board.
	:param input_data: (lst) The nested list of a given word list input by user.
						For example:
						1 row of letters: [["f","y","c","l"],  [(0, 0), (0, 1), (0, 2), (0, 3)]
						2 row of letters:  ["i","o","m","g"],  [(1, 0), (1, 1), (1, 2), (1, 3)]
						3 row of letters:  ["o","r","i","l"],  [(2, 0), (2, 1), (2, 2), (3, 3)]
						4 row of letters:  ["h","j","h","u"]]  [(3, 0), (3, 1), (3, 2), (3, 3)]
	"""

	for x in range(4):
		for y in range(4):
			word = []   				   							  # a word list, e.g. ['f', 'y', 'c', 'l']
			pos = []    				   							  # a list stores tuple, e.g. [(0, 0), (0, 1)]
			word.append(input_data[x][y])  							  # decide the first character
			pos.append((x, y))            							  # the position (x,y) of the first character

			search_helper(x, y, word, pos, input_data)  			  # search letters with specific first character


def search_helper(x, y, word, pos, input_data):
	"""
	A helper to find a set of words on the board.

	:param x: (int) The x-axis(row) of a position .
	:param y: (int) The y-axis(column) of a position.
	:param word: (list) A list that contains letter.
	:param pos: (tuple) A 2-tuple giving row and column of a position.
	:param input_data:The nested list of a given word list input by user.
	"""

	if len(word) >= 4:                                                 # Base case
		if "".join(word) not in found_words:
			if has_prefix("".join(word)):
				# if four-letter words in dictionary
				if "".join(word) in dict_list:
					print(f'Found: "{"".join(word)}"')
					found_words.append("".join(word))
					finding_longer_words(x, y, word, pos, input_data)  # words with more than four letters

				# if four-letter words not in dictionary
				else:
					words_more_than_four_char(x, y, word, pos, input_data)

	# when word is less than four letters
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 4 > i >= 0 and 4 > j >= 0:
					if (i, j) not in pos:
						# Choose
						word.append(input_data[i][j])
						pos.append((i, j))
						# Explore
						search_helper(i, j, word, pos, input_data)
						# Un-choose
						word.pop()
						pos.pop()


def words_more_than_four_char(x, y, word, pos, input_data):
	"""
	To find words with more than four letters and exists in dictionary.
	E.g. "happ" is not a word, but "happy" is.

	:param x: (int) The x-axis(row) of a position .
	:param y: (int) The y-axis(column) of a position.
	:param word: (list) A list that contains letter.
	:param pos: (tuple) A 2-tuple giving row and column of a position.
	:param input_data:The nested list of a given word list input by user.
	"""
	if "".join(word) not in found_words and "".join(word) in dict_list:  # Base case
		print(f'Found: "{"".join(word)}"')
		found_words.append("".join(word))
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 4 > i >= 0 and 4 > j >= 0:
					if (i, j) not in pos:
						# Choose
						word.append(input_data[i][j])
						pos.append((i, j))
						# Explore
						words_more_than_four_char(i, j, word, pos, input_data)
						# Un-choose
						word.pop()
						pos.pop()


def finding_longer_words(x, y, word, pos, input_data):
	"""
	To find words with more than four letters after finding four-letters words in dictionary.
	E.g. already found "room", but keep finding longer words like "roomy".

	:param x: (int) The x-axis(row) of a position .
	:param y: (int) The y-axis(column) of a position.
	:param word: (list) A list that contains letter.
	:param pos: (tuple) A 2-tuple giving row and column of a position.
	:param input_data: The nested list of a given word list input by user.
	"""
	if "".join(word) not in found_words and "".join(word) in dict_list:  # Base case
		print(f'Found: "{"".join(word)}"')
		found_words.append("".join(word))
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 4 > i >= 0 and 4 > j >= 0:
					if (i, j) not in pos:
						# Choose
						word.append(input_data[i][j])
						pos.append((i, j))
						# Explore
						finding_longer_words(i, j, word, pos, input_data)
						# Un-choose
						word.pop()
						pos.pop()


def test_input(letter):
	"""
	To check whether the user inputs correctly.

	:param letter: (str) The letter user inputs.
	:return: Bool, The input is correct or not.
	"""
	if len(letter) == 7:                                                    # four letters + three spaces
		letter = letter.replace(" ", "")
		if len(letter) == 4 and letter.isalpha():         				    # when user inserts letters correctly
			return True
		else:                                                               # when user inserts letters incorrectly
			print("Illegal input! Please insert space between letters.")
			return False
	else:                                                                   # when user inserts letters incorrectly
		print("Illegal input! Please insert four letters in one row.")
		return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:          							 # pruning unnecessary words
				dict_list.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s:(str) A substring that is constructed by neighboring letters on a 4x4 square grid.
	:return Bool: If there is any words with prefix stored in sub_s, return True.
	"""
	for item in dict_list:
		if item.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
