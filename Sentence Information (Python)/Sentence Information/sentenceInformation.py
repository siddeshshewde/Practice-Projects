def main():
	input = "Hello World! The most basic program in any language - 10 stars to Python :)"

	print ("The sentence is:")
	print(input)
	
	character = 0
	vowel = 0
	cons = 0
	words = 1 
	digits = 0
	special = 0
	
	#List of special characters to be considered
	sp = '!@#$%^&*_=+-/.?<>()'


	for i in input:
		character += 1
		if i in sp:
			special += 1    
		elif i >='0' and i <= '9':
			digits += 1
		elif i == ' ':
			words += 1
		elif i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
			vowel += 1
		else:
			cons += 1

	print("\nInformation:")
	print ("Characters: {}".format(character))
	print ("Vowels: {}".format(vowel))
	print ("Consonants: {}".format(cons))
	print ("Words: {}".format(words))
	print ("Digits: {}".format(digits))
	print ("Special Characters: {}".format(special))

main()
