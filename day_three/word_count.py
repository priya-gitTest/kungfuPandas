article = open("article.txt", encoding="latin-1")

top_numbers = int( input("How many most common words do you want?") )

words = {}

top_word =[]

running = True

#Read each line of text file untill no lines remain
while running == True:
	
	#Read next line of text file
	current_line = article.readline() 

	#Makes a list of words by splitting string on spaces
	line_words = current_line.split(" ")


	#Reads each word and puts it in a dictionary
	for current_word in line_words:
		#IF the word only contains letters insert into dictionary
		if current_word.isalpha() == True:
			if words.get(current_word) == None:
				words[ current_word ] = 1
			else:
				words[current_word] = words[current_word] + 1
		#Remove all symbols and insert into dictionary
		else:

			new_string = ""
			#Removes all new line characters
			current_word = current_word.replace("\n","")
			#removes all utf-8 encoded characters
			current_word = bytes(current_word, 'utf-8').decode('utf-8','ignore')

			# print(current_word)

			#Removes any symbols and numbers
			for letter in current_word:
				if letter.isalpha() == True:
					new_string = new_string + letter

			#Inserts cleaned word into dicitonary
			if new_string != "":
			# if len(new_string) > 0:
				if words.get(new_string) == None:
					words[ new_string ] = 1
				else:
					words[new_string] = words[new_string] + 1

	#At end of file stop while loop
	if current_line == "":
		running = False

# print(words)

#Fills list with keys and sorts list
for key, value in words.items():
	#If the list is empty insert first word into list
	if len(top_word) == 0:
		top_word.append(key)

	#Inserts items into list and sorts them
	else:

		#If list has less items than user requests, sort the current word in and insert even if current_word is lower than all others 
		if len(top_word) < top_numbers:
			for x in range( len(top_word) ):
				
				if value >= words[ top_word[x] ]:
					top_word.insert(x, key)
					break
				elif x == len(top_word)-1:
					top_word.append(key)

		#When the list is full sort words in if  larger than words in list or smaller ignore
		else:
			for x in range( len(top_word) ):
				
				if value >= words[ top_word[x] ]:
					top_word.insert(x, key)
					top_word.pop()
					break

#Output
for key in top_word:
	print(key + ":" + str( words[ key ] )  )