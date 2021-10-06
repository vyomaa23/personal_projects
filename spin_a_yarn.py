import random

pl = True
with open('rand.text', "r") as file:
	text = file.read()
	all_words = list(map(str, text.split()))
	if pl == True:
		rando = random.choice(all_words)
	else:
		rando = random.choice(all_words)
	print(f'{rando}: len: {len(rando)} word: {rando[2]}')	

empty = []
str = ''
play = True
while len(empty) < len(rando):
	for char in rando:
		empty.append(char)
		# if i % 2 != 0:
		# 	rando(i) = '_'

for i in range (len(empty)):
	if i%2 != 0:
		empty[i] = '_'
	str += empty[i]

play_active = True
print('Welcome to "Guess a Country!!"')
print('I will show you an incomplete name of a country, you gotta guess what country it is!')
while play_active:
	user_in = input(f'Incomplete word: "{str.upper()}" \nComplete Word: ')
	if user_in.upper() == rando.upper():
		print('Great job! You guessed it right.')
		play_active = False
	else:
		print("Guess again!")

		










