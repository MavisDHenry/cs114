from random import randint

print('what is your name?')
myname = input()
if myname == 'Mavis':
    print('Hi sweetie want to date?')
else:
    print('ha ha your name sucks...')
print('any way how old are you?')
myage = input()
if myage == '25':
    print('your as old as the Mavis I know.')
else:
    print('man thats old... or is it... Oh well')
print('what is your question?')
myquestion = input()
print(str(myquestion) + ' is that all you want to ask? no? well to bad one'
      ' question at a time.')
eight_ball = randint(1 , int(myage) * int(len(myname)))
if eight_ball < 5:
    print('Awww you just a sweet little baby arn\'t you?')
elif eight_ball < 10:
    print('Well look at that your lucks turned to fish.')
elif eight_ball < 15:
    print('My oh my it looks like you get nothing try again.')
elif eight_ball < 20:
    print('You almost made it past your problem but then you got eaten.')
elif eight_ball < 30:
    print('baseballs are cool right, unless they hit you in the head...'
    ' might want to duck')
else:
    print('sorry i\' way to high right now go ask some one else for the answer.')
