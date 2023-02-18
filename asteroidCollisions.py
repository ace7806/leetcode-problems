Asteroids = [-10, 5, -10, -30, 30, -4, -30, 500] # = -10 -10 -30 500
Asteroids2 = [500,8,-8,8,-8,8,-8,8,-8,8,-8,8,-8,8,-8,-4000] # = -10 -10 -30 500

'''
have a stack for asteroids going to the right
if stack is empty and asteroid is going to the left it means it has left unscathed and we can add to the output list
if asteroid is negative consume from stack until it it crahses with an asteroid or stack is empty
'''

def stateOfAsteroids(asteroids):
       stack = []
       asteroidState = []
       for asteroid in asteroids:
              if asteroid < 0:
                     while stack and stack[-1] < abs(asteroid): stack.pop()
                     if stack and stack[-1]==abs(asteroid): stack.pop()
                     elif not stack: asteroidState.append(asteroid)
              else: stack.append(asteroid)
       asteroidState.extend(stack)
       return asteroidState
print(stateOfAsteroids(Asteroids))
print(stateOfAsteroids(Asteroids2))