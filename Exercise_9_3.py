def avoids(word, forbidden):

	for letters in word:

		if forbidden in word:

			return False

	return True

avoids(“dollyanusha”, “am”)
