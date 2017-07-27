
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
            print('your hands froze but otherwise your fine')
    elif mymove1 == ('sword'):
        print('you cut the snowflake pile in half creating two!')
        print('the snowflake piles attack with killer intent.')
        print('can fight or run what will you do')
        mymove2 = input
        if mymove2 ==('fight'):
            print('you charge into battle which do you attack pile1 or pile2?')
            attack = input()
            if attack == ('pile1'):
                print('you kill pile1, pile2 attacks you lose warmth')
                print('you can run or fight')
                attack1 = input()
                if attack1 == ('fight'):
                    print(' you kill pile2 leaving you cold but alive')
                elif attack1 == ('run'):
                    print('you flee cold and afraid but at least your alive')
            elif attack == ('pile2'):
                print('pile2 was killed pile1 becomes enraged!')
                print('you can either run or fight')
                attack1 = input()
                if attack1 == ('fight'):
                    print('Alas brave adventurer you have subcummed to the'
                          'dread cold')
                    print("its enraged probly should've ran")
                elif attack1 == ('run'):
                    print('you escape the raging pile of snoflakes but for how'
                          ' long?')
        elif mymove2 == ('run'):
            print('you escape the piles of snowflakes.')
elif mymove == ('sword'):
    print('snowflake is cut in half')
    print('a pile of snowflakes attempts to run away from you')
    myact = input()
    if myact == ('chase'):
        print('you catch up to the pile of snowflakes')
        print('whar will you do? kill or spare.')
        myact1 = input()
        if myact1 == ('kill'):
            print('you take your sword and procede to cut the pile of '
                  'snowflakes into tiny peices')
            print('you walk away knowing the snowflakes are no more')
        elif myact1 == ('spare'):
            print('you pat the pile of snowflakes on the head and walk away.')
    else:
        print('the pile of snowflakes got away...')
else:
    print('you were mercilessly cut down by the snowflake your journey'
          ' comes to a close')
print('a portal to a new world opens up what will you do?')
myaction = input()
if myaction in ('jump in' , 'go in' , 'use portal'):
    print('you jump into the portal without hesitation')
else:
    print('the game is over try another route maybe try sword, hug or chase.')
