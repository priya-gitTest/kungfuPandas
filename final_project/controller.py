from view import View

my_view = View()

def toPigLatin():
	sentence = my_view.takeInput("Enter a Sentence: ")
	sentence = sentence.split(" ")
	new_sentence = []
	vowel = ["a","e","i","o","u"]
	for word in sentence:

		if word[0].lower() in vowel:
			new_sentence.append( word+"-ay" )
		else:
			for index in range( len(word) ):
				if word[index].lower() in vowel:
					consonant = word[0:index]
					remainder = list(word[index:])
					for x in range( len(remainder)-1,-1,-1):
						if remainder[x].isalpha() == True:
							remainder.insert(x+1, "-"+consonant + "ay")
							remainder = "".join(remainder)
							new_sentence.append(remainder)
							break

					break
	my_view.printOut( " ".join(new_sentence) )


def fromPigLatin():
	sentence = my_view.takeInput("Enter a Sentence: ")
	sentence = sentence.split(" ")
	new_sentence = []
	for word in sentence:
		parts_of_word = word.split("-")
		ay = parts_of_word.pop()
		ay_index = ay.rfind("ay")
		before_ay = ay[0:ay_index]
		after_ay = ""
		if ay_index+2 <= len(ay)-1:
			after_ay = ay[ay_index+2: ]
		parts_of_word[0] = before_ay + parts_of_word[0]
		new_sentence.append( "-".join(parts_of_word)+after_ay )

	my_view.printOut( " ".join(new_sentence) )



fromPigLatin()
# toPigLatin()
