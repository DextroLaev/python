print()
no_of_sticks = int(input('Enter the no. of sticks with which you to play:- '))
print('|'*no_of_sticks)

def stick(no_of_sticks):
    print('|'*no_of_sticks)
    
player_turn = 1
player_A = input('player A enter your name:- ')    
player_B = input('player B enter your name :- ')

def turn(player_turn):
    if player_turn%2==1:
        player = player_A
    elif player_turn%2==0:
        player = player_B
    return player

while True:
    if no_of_sticks>1:
        current_player = turn(player_turn)
        sticks = int(input("{} please select no. of sticks:- ".format(current_player)))
        while (sticks > 4):
            if (sticks > 4):    
                print('please select sticks within the given range.')
                stick(no_of_sticks)
                sticks = int(input("{}  please select no. of sticks:- ".format(current_player))) 
        no_of_sticks = no_of_sticks-sticks
        print()
        stick(no_of_sticks)
        player_turn+=1        
    else:
        current_player = turn(player_turn-1)
        print()
        print('{} you won the match'.format(current_player))
        break
            