from random import seed
from random import randint


guess_flag = True
value = randint(1,100)
while guess_flag:
	user_in = input('Guess which number I am thinking: ')
	if int(user_in) == value:
		print('Congrats, you guessd it right')
		loop = input('Wanna play again? (Yes/No): ')
		if loop.title() == 'No':
			guess_flag = False
		else:
			value = randint(50,200) 
	else:
		print('Wrong, wanna guess again? Guess a bigger number!')
		hint = abs(int(user_in) - value)
		print(f'\nHint: Your input is {hint} far off from the number I am thinking. Guess again!')
	