import random

def get_choice(c):
	rps = {
		"R": "Rock",
		"P": "Paper",
		"S": "Scissors"
	}
	return rps[c]

def main():
	global pname
	choices = ['R', 'P', 'S']

	cpu_choice = random.choice(choices)

	player_choice = input('Select your option R | P | S: ').upper()
	while player_choice not in choices:
		print("Invalid choice, try again.")
		player_choice = input('Select your option R | P | S: ').upper()
		
	if player_choice == cpu_choice:
		print(f'Player ({get_choice(player_choice)}) : CPU ({get_choice(cpu_choice)}) - It\'s a tie.')
		main()
	else:
		winner = ''
		if player_choice == 'R':
			if cpu_choice == 'P':
				winner = "CPU"
			else:
				winner = pname
		elif player_choice == "P":
			if cpu_choice == "S":
				winner = "CPU"
			else:
				winner = pname
		elif player_choice == "S":
			if cpu_choice == "R":
				winner = "CPU"
			else:
				winner = pname

		print(f'Player ({get_choice(player_choice)}) : CPU ({get_choice(cpu_choice)})')
		if winner == pname:
			print(f'You win - Winner ({winner})')
		else:
			print("Your lose to CPU.")

if __name__ == "__main__":
	print("**************************************\n* Welcome to Rock, Paper & Scissors. *")
	print("*           My name is CPU           *")
	print("**************************************\n")

	pname = input("What shall I call you ? ")

	print(f'{pname}, It\'s nice to have you here.')
	main()