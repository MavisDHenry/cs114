from random import randint
print('Hello my name is donut whats yours?')
myname = input()
for item in range(randint(1,20)):
    print(str(myname))
    if item < 5:
        print('ate cake')
    elif item > 5:
        print('ate pie')
    else:
        print('ate themselves')
