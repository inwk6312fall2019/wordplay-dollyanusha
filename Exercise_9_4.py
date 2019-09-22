def uses_only(word, string_of_letters):

	for letter in word:

		if letter not in string_of_letters:

			return False

	return True
