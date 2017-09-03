from random import randint
answers = ['Awww you just a sweet little baby arn\'t you?',
           'Well look at that your lucks turned to fish.',
           'Who are you really... don\'t answer that i don\'t need to know.',
           'My oh my it looks like you get nothing try again.',
           'You almost made it past your problem but then you got eaten.',
           'baseballs are cool right, unless they hit you in the head...'
           ' might want to duck',
           'Holy poopballs that sucks... to bad you\'ll never know what',
           'Sorry i was asleep could you repeat that?',
           'Ok here is the deal you have no luck at all and'
           'will probably die in the near future... seriously look out.',
           'sorry i\'m way to high right now go ask some one else for the answer.']

def magic8ball_question_question():
    myquestion = input('What is your question? ')
    eight_ball = randint(1 , int(len(myquestion)))
    return eight_ball




def magic8ball_answers(eight_ball):
    return print(answers[randint(0, int(eight_ball))])



def main():
    eight_ball = magic8ball_question_question()
    return magic8ball_answers(eight_ball)

main()
