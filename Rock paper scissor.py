## Rock Paper Scissor game by Ayaan Ul Hasan


import random
from time import sleep

hand_state = ['Rock','Paper','Scissor']
running = True

def win():
    global pl_score 
    print('You won, 3 point to you\n')
    pl_score += 3

def lose():
    global pc_score
    print('You loss, 3 point to me\n')
    pc_score += 3
    
def draw():
    global pl_score
    global pc_score
    print('Draw, 1 point to both\n')
    pl_score += 1
    pc_score += 1

def end():
    print(f'\nYour score: {pl_score}')
    print(f'My score: {pc_score}')
    
    if pl_score > pc_score:
        print('Congrats! you Won!!')
    elif pl_score < pc_score:
        print('You loss! better luck next time')
    else:
        print('It\'s a Draw :)')
    sleep(5)

print('Welcome to Rock Paper Scissor by Ayaan Ul Hasan')

pl_score = 0
pc_score = 0

while running:

    print('1: Rock\n2: Paper\n3: Scissor\n4: Quit')
    player_choice = int(input('Enter the number infront to lock your choice: '))

    if player_choice == 4:
        sleep(1)
        end()
        break
    elif player_choice > 4 or player_choice < 1:
        print('Invalid input, try again\n')
        continue
    else:
        player_choice = hand_state[player_choice-1]
    
    pc_choice = random.choice(hand_state)

    sleep(1)
    print('\nYou choose:',player_choice)
    print('I choose:',pc_choice)

    sleep(1)
    if player_choice == pc_choice:
        draw()
    elif player_choice == 'Rock' and pc_choice == 'Scissor':
        win()
    elif player_choice == 'Rock' and pc_choice == 'Paper':
        lose()
    elif player_choice == 'Paper' and pc_choice == 'Scissor':
        lose()
    elif player_choice == 'Paper' and pc_choice == 'Rock':
        win()
    elif player_choice == 'Scissor' and pc_choice == 'Rock':
        lose()
    elif player_choice == 'Scissor' and pc_choice == 'Paper':
        win()
    
