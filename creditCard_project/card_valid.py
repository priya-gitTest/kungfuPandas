class CreditCard:
    
    def __init__(self, card_number):
    	pass

    	# write your code here


























# #do not modify assert statements

# cc = CreditCard('9999999999999999')

# assert cc.valid == False, "Credit Card number cannot start with 9"
# assert cc.card_type == "INVALID", "99... card type is INVALID"

# cc = CreditCard('4440')

# assert cc.valid == False, "4440 is too short to be valid"
# assert cc.card_type == "INVALID", "4440 card type is INVALID"

# cc = CreditCard('5515460934365316')

# assert cc.valid == True, "Mastercard is Valid"
# assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

# cc = CreditCard('6011053711075799')

# assert cc.valid == True, "Discover Card is Valid"
# assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

# cc = CreditCard('379179199857686')

# assert cc.valid == True, "AMEX is Valid"
# assert cc.card_type == "AMEX", "card_type is AMEX"

# cc = CreditCard('4929896355493470')

# assert cc.valid == True, "Visa Card is Valid"
# assert cc.card_type == "VISA", "card_type is VISA"

# cc = CreditCard('4329876355493470')

# assert cc.valid == False, "This card does not meet mod10"
# assert cc.card_type == "INVALID", "card_type is INVALID"

# cc = CreditCard('339179199857685')

# assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
# assert cc.card_type == "INVALID", "card_type is INVALID"