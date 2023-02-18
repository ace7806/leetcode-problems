from random import randrange
playerCounter = 0
aiCounter = 0
while 1:
    player = int(input('0 for ROCK, 1 for PAPER, 2 for SCISSORS: '))
    ai = randrange(3)
    print('ai chose: ' + str(ai))
    if player == ai: print('tie')
    elif (player ==0 and ai==2) or (player == 1 and ai==0) or (player == 2 and ai==1):
         print('player won')
         playerCounter+=1
    else:
         print('ai won')
         aiCounter+=1
    print('player: '+ str(playerCounter) + ' AI: ' + str(aiCounter))
