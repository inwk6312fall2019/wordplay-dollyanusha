def words_has_no_e():

	myfile=open(“words.txt”,’r’)

	for line in myfile:

		if line.find(“e”) == -1:

			return(“True”)

def fun_has_no_e():

	myfile=open(“words.txt”)
    count = 0

	total_words = 0

	for line in myfile:

		total_words = total_words + 1

		words = line.strip()

		if words.find(“e”) == -1:

			print(words)

			count = count +1

	percent_of_words = (count/total_words)*100

	print(“Percent:”, percent_of_words)
