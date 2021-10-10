# Rock Paper Scissor
""" In the begining the user will input how many matches will be played in the whole series.
One by one the user and the computer will play. If a match is tie, it won't be counted in the final tally. 
The winner of the series will be anounced in the end. """


import random
print('Welcome to "Rock Paper Scissor"!')

while True:
	try:
		turn = int(input("Type the number of matches you would like to play to complete the series: "))
		break
	except ValueError:
		print("\nPlease input integer only...")
		continue  

print(f'\nTotal Turns: {turn}')
rec = []
game_active = True
counter = 1
while counter <= turn:
    vars = 'rock paper scissor'
    moves = list(map(str, vars.split()))
    com_move = random.choice(moves)
    # print(f'My move: {com_move}')
    user_move = input(f'\nYour Move: ')
    user_move = user_move.lower()

    if ((com_move == 'rock' and user_move == 'scissor') or (com_move == 'paper' and user_move == 'rock') or (com_move == 'scissor' and user_move == 'paper')):
    	if counter <= turn:
    		print(f'My move: {com_move}')
    		print(f'I Won match {counter}')
    		rec.append('C')
    	else:
    		game_active = False  	
    elif com_move == user_move:
    	if counter <= turn:
    		print(f'My move: {com_move}')
    		print("It's a tie, play again!")
    		counter -= 1
    	else:
    		game_active = False
    elif (user_move == 'rock' and com_move == 'scissor') or (user_move == 'paper' and com_move == 'rock') or (user_move == 'scissor' and com_move == 'paper'):
    	if counter <= turn:
    		print(f'My move: {com_move}')
    		print(f'You Won match {counter}')
    		rec.append('U')
    	else:
    		game_active = False
    else: 
    	
    	print('Invalid move, try again!')
    	if counter <= turn:
    		print('Not a valid move!')
    		counter -= 1
    	else:
    		game_active = False  
    counter += 1

    len_c = 0 
    len_r = 0
    for item in rec:
    	if item == 'C':
    		len_c += 1
    	else:
    		len_r += 1


print ("\n--------------------Match Results------------------")

n = len(rec) + 1
for i in range (1, n):
	print(f'Match {i} winner: {rec[i-1]}')
print(f'\nTotal matches played: {turn}')
print(f'I won {len_c} and you won {len_r}')
if len_r > len_c:
	print("\nYOU WON THE SERIES, CONGRATS!")
elif len_r < len_c:
	print("\nI WON THE SERIES..YEEE!")
else:
	print('\nSERIES WAS A TIE!\n')
