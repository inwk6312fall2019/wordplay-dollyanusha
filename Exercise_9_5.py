def uses_all(word, required_letters):

	for letter in required_letters:

		if letter not in word: 

			return False

	return True
