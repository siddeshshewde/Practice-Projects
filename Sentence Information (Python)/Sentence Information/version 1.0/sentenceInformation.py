
def main():
	input = " Hello World! The most basic program in any language :)"

	print ("The sentence is:")
	print(input)
	print ("Characters: {}".format(characters(input)))
	print ("Vowels: {}".format(vowels(input)))
	print ("Consonants {}:".format(consonants(input)))
	print ("Words: {}".format(words(input)))
	print ("Digits: {}".format(digits(input)))
	#print ("Special Characters: {}".format(special(input)))




def characters (input):
	character = 0
	for i in input:
		char += 1
		return character

def vowels (input):
	vowel = 0
	for i in input:
		if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
			vowel += 1
	return vowel

def consonants (input):
	cons = 0
	for i in input:
		if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
			pass
		else:
			cons += 1
	return cons

def words (input):
	words = 1
	for i in input:
		if i == ' ':
			words += 1
	return words

def digits (input):
	digits = 0
	for i in input:
		if i >= 0 and i <= 9:
			digits += 1
	return digits

#def special (input):
main()
