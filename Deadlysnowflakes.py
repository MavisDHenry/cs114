
possible_moves = {'right', 'left'}
move_q = "Do you want to move {} or {}? ".format(*possible_moves)

print('Death to snowflakes')
print('a snowflake approches at an extremely high velocity')
mymove = input(move_q)
if mymove in possible_moves:
    print('you narrowly avoided the deadly snowflake')
    print('a pile of snowflakes gingerly falls towards you')
    mymove1 = input(move_q)
    if mymove1 in possible_moves:
        print('the snowflake pile cries as you dodge its embrace')
    elif mymove1 == ('hug'):
        print('the pile of snowflakes smothers you in its gentle cold embrace')
        print('how long do you embrace?')
        mytime = input()
        if int(mytime) < 30:
            print('you feel cold but otherwise your alright')
            print('you have succesfully befriended the snowflake pile')
        elif int(mytime) > 30:
            print('you freeze to death thus ending you adventure')
        else:
            print('woo hoo')
elif mymove == ('sword'):
    print('snowflake is cut in half')
    print('a pile of snowflakes attempts to run away from you')
    myact = input()
    if myact == ('chase'):
        print('you catch up to the pile of snowflakes')
