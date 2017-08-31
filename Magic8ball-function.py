from random import randint

def magic8ball_question_name():
    myname = input('what is your name? ')
    return myname

def magic8ball_question_age():
    myage = input('Any way how old are you? ')
    return myage

def magic8ball_question_question():
    myquestion = input('What is your question? ')
    eight_ball = randint(1 , int(magic8ball_question_age()) * int(len(magic8ball_question_name())))
    return eight_ball

def magic8ball_answers(eight_ball):

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
    elif eight_ball < 40:
        print('Holy poopballs that sucks... to bad you\'ll never know what')
    elif eight_ball < 50:
        print('Sorry i was asleep could you repeat that?')
    elif eight_ball < 60:
        print('Ok here is the deal you have no luck at all and'
              'will probably die in the near future... seriously look out.')
    else:
        print('sorry i\'m way to high right now go ask some one else for the answer.')


def main():
    eight_ball = magic8ball_question_question()
    return magic8ball_answers(eight_ball)

main()
