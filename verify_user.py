# Verify User
"""The program will remember the username which was last used and will ask the new user if the last used user ame 
belongs to themif not, a new username will be creayed."""


def get_stored_username():
	filename = 'username.json'
	try:
		with open (filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:                         #else block is to print the output from the try block
		return username

def new_username(username):
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def verify_user():
	username = get_stored_username()
	if username:
		correct_name = input(f'Is this username yours(y/n)? \nUsername - {username} : ')
		if correct_name == 'y':
			print(f'Welcome back, {username}')
		else:
			username = input('Please enter your new username: ')
			username = new_username(username)
			print(f"we will rememer this user name next time, {username}")

	else:
		username = input('Please enter your new username: ')
		username = new_username(username)
		print(f"we will rememer you next time, {username}")

verify_user()