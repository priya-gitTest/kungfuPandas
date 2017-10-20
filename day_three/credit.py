class CreditCard:
	number = str()
	card_type= str()
	valid = bool()

	def __init__(self, card_num):
		self.number=card_num
		self.checkLength()

	def checkLength(self):
		if len(self.number) == 16 or len(self.number) == 15:
			self.cardType()
		else:
			self.valid = False
			self.card_type = "INVALID"

	def cardType(self):
		card_companies = {"4":"VISA","51":"MASTER CARD","52":"MASTER CARD","53":"MASTER CARD","54":"MASTER CARD","55":"MASTER CARD","6":"DISCOVER","34":"AMEX","37":"AMEX"}

		for startingchar in card_companies.keys():
			if self.number[0: len(startingchar) ] == startingchar:
				self.card_type = card_companies[startingchar]
				break

		if self.card_type == str():
			self.valid = False
			self.card_type = "INVALID"
		else:
			card_length = {"VISA":16, "MASTER CARD":16,"DISCOVER":16,"AMEX":15}
			if len(self.number) == card_length[ self.card_type ]  and self.number.isdigit()==True:
				self.luhn()
			else:
				self.valid = False
				self.card_type = "INVALID"


	def luhn(self):
		num_list = []
		to_double = False
		for x in range(len(self.number)-1, -1, -1):
			if to_double == False:
				num_list.append( int( self.number[x] ) )
				to_double=True
			else:
				num_list.append( int( self.number[x] )*2 )
				to_double=False

		luhn_num = 0
		for index in num_list:
			if index >= 10:
				luhn_num = luhn_num + 1 +(index-10)
			else:
				luhn_num = luhn_num + index

		if luhn_num % 10 == 0:
			self.valid = True
		else:
			self.valid = False

mycard = CreditCard("401234567890123")