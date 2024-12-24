import random
user_wins = 0 #number of times user win the games
computer_wins = 0 #number of times user computer the games
options = ['rock','scissors','paper'] #possible outcomes

while True:
    user_input = input('Type Rock/Paper/Scissors or Quit to exit : ').lower() #taking users input and changing it to lower case

#checking if user wants to quit the game
    if user_input == 'q':
        print('Thanks for playing. Hope you enjoyed')
        break
#chacking for invalid input
    if user_input not in options:
        print('Invalid input')
        continue

    number = random.randint(0,2)

#deciding computers input
    computer_option = options[number]
    print(f'computer plays {computer_option} you play {user_input}') 

#checking all possible combinations of wining or losing or drawing
    if user_input == 'rock' and computer_option == 'scissors':
        print('you win')
        user_wins +=1
        
    elif user_input == 'paper' and computer_option == 'rock':
        print('you win')
        user_wins +=1
        
    elif user_input == 'scissors' and computer_option == 'paper':
        print('you win')
        user_wins +=1

    elif user_input == computer_option:
        print('draw')

    else:
        print('computer wins')
        computer_wins +=1

#displaying the number of times user won and number of times computer won the game
print(f'{user_wins} v/s {computer_wins}')
print('Good Bye')