word_file = open("letters.txt")

word_dictionary = {}

running = True

while running == True:

	read_line = word_file.readline()

	for letter in read_line:
		if word_dictionary.get(letter) == None:
			word_dictionary[ letter ] = 1
		else:
			word_dictionary[letter] = word_dictionary[letter] + 1

	if read_line == "":
		running = False

print(word_dictionary)