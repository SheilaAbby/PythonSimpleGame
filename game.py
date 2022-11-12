import random

def get_choices(): 
    player_choice = input('Choose (paper, rock or scissors)')
    options = ['paper', 'rock', 'scissors']
    computer_choice = random.choice(options)

    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    print(f'You chose {player}, Computer chose {computer}')

    if player == computer:
        return ("It's a tie!")
    elif player == 'rock':
        if computer == 'paper':
            return ('Paper Covers Rock, You lose.')
        else:
            return ('You Win! Rock smashes Scissors')

    elif player == 'paper':
        if computer == 'scissors':
            return ('Scissors cuts Paper, You lose.')
        else:
            return ('Rock cuts Paper, You lose.')
  
    elif player == 'scissors':
        if computer == 'paper':
            return ('You Win! Scissors cuts Paper')
        else:
            return ('Rock smashes Scissors, You lose.')
            
    else:
        return ('No Match! Check the spelling of your selected choice')

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)