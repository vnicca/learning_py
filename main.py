'''Rock_Scissors_Paper_Lizard_Spock'''
import random
flag = True
while flag:
    flag = False

    player_choice = ''
    bot_choice = ''
    player_score = 0
    bot_score = 0
    
    for i in range(1, 5+1):
        print(f'ROUND {i}')
        player_choice = str(input('Enter choice : [r], [p], [s], [l], [k] :'))
        bot_choice = random.choice('rpslk')
        print(f'Player"s choice : {player_choice}.\nBot"s choice : {bot_choice} ')

        if player_choice == bot_choice:
            print('Draw round')
        elif player_choice == 'r':
            if bot_choice == 'k' or bot_choice == 'p':
                print('Bot wins the round')
                bot_score = bot_score + 1
            else:
                print('Player wins the round')
                player_score = player_score+1
        elif player_choice == 'p':
            if bot_choice == 'r' or bot_choice == 'k':
                print('Player wins the round')
                player_score = player_score + 1
            else:
                print('Bot wins the round')
                bot_score = bot_score+1
        elif player_choice == 's':
            if bot_choice == 'p' or bot_choice == 'l':
                print('Player wins the round')
                player_score = player_score + 1
            else:
                print('Bot wins the round')
                bot_score = bot_score+1
        elif player_choice == 'k':
            if bot_choice == 'r' or bot_choice == 's':
                print('Player wins the round')
                player_score = player_score + 1
            else:
                print('Bot wins the round')
                bot_score = bot_score+1
        elif player_choice == 'l':
            if bot_choice == 'p' or bot_choice == 's':
                print('Player wins the round')
                player_score = player_score + 1
            else:
                print('Bot wins the round')
                bot_score = bot_score+1
    if player_score >  bot_score:
        print(f'Player wins the battle with score : {player_score} :  {bot_score} ')
    elif player_score <  bot_score:
        print(f'Bot wins the battle with score : {bot_score} :  {player_score} ')
    elif player_score ==  bot_score:
        print(f'the score is equal : {player_score} :  {bot_score} ')
    else:
        print('Smthing is going wrong')
    flag = bool(input("Press [Any key] + [Enter] to continue : "))
