playerhp = {'level_1': 100, 'level_2': 110, 'level_3': 120, 'level_4': 130,
            'level_5': 140, 'level_6': 150, 'level_7': 160, 'level_8': 170,
            'level_9': 180, 'level_10': 200}
flamehp = 200
currentflamehp = flamehp
currentplayerhp = playerhp['level_1']
beastiary = {'minor_flame': 200, 'medium_flame': 250, 'major_flame': 300,
             'fire_walker': 500, 'flame_warden': 700, 'flame_devil': 1000}
print('hello your about to enter a world of burning or a building that\'s on '
      'fire')
print('your sword has turned into a torrent of water just in the shape of a'
      ' sword')
print('you start in a room with a door will you go through?')
myanswer = input()
if myanswer == 'yes':
    print('you walk through the door into a hallway that is covered in flame')
    print('will you approach the flame?')
    myanswer = input()
    if myanswer == 'yes':
        print('The flame attacks')
        while currentflamehp > 0:
            print('you can fight the flame, or run from the flame what'
                  ' will you do?')
            myact = input()
            if myact == "fight":
                currentflamehp -= 25
                print(currentflamehp)
                currentplayerhp -= 5
                print(currentplayerhp)
                if currentplayerhp == 0:
                    print("you have died by burning")
                    break
            elif myact == "run":
                print('you flee from the flame only to be cornered.')
                print('will you fight or be engulfed by the flame.')
                myact = input()
                if myact == 'fight':
                    continue
                else:
                    print('you have been burned to death!')
                    quit()
            else:
                print('the flame engulfs you')
                quit()
    print('you have gained a level you can now use the heal command in battle.')
    currentplayerhp = playerhp['level_2']
    print('you come to a fork in the hallway. will you go left or right?')
    mymove= input()
    if mymove == "right":
        print('you come to a door will you open it?')
        myanswer = input()
        if myanswer == 'yes':
            print('you enter a room with a flame warden, will you fight or run?')
            myact = input()
            if myact == 'fight':
                print('The flame warden attacks dealing 8 dmg.')
                currentplayerhp -= 8
                currentflamehp = beastiary['flame_warden']
                while currentflamehp > 0:
                    myact = input()
                    if myact == 'fight':
                        currentflamehp -= 25
                        print('flame warden hp ' + str(currentflamehp))
                        currentplayerhp -= 8
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                    elif myact == 'heal':
                        if currentplayerhp >= playerhp[level_2]:
                            print('your already at max hp')
                            return
                        else:
                            currentplayerhp += 10
                            print('the flame warden retaliates with an attack.')
                            currentplayerhp -= 8
                            print('your hp ' + str(currentplayerhp))
                            if currentplayerhp < 0:
                                print('alas you have died by the flame')
                                quit()
                    elif myact == 'run':
                        print('you flee from the flame warden in terror '
                              'only to be caught by him moments later')
                        currentplayerhp -= 8
                        print('you' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                    else:
                        currentplayerhp -= 8
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                print('you have defeated the flame warden.')
                print('the game is now over good job doing things the hard way.')
                quit()
            else:
                print('you run straight past the flame warden straight into the'
                      'fire devil')
                myact = input()
                print('you have died to the true final boss play the long route'
                      'to actually stand a chance.')
                quit()

    elif mymove == 'left':
        print('you meet a minor flame will you approach?')
        myanswer = input()
        if myanswer == 'yes':
            currentflamehp = beastiary['minor_flame']
            while currentflamehp > 0:
                print(' you have engaged in battle with the minor flame you can '
                      'fight, run, or heal, what will you do?')
                myact =input()
                if myact == "fight":
                    currentflamehp -= 30
                    print('minor flame ' + str(currentflamehp))
                    currentplayerhp -= 5
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('alas brave adventurer you have been incinerated.')
                        quit()
                elif myact == 'heal':
                    if currentplayerhp >= playerhp[level_2]:
                        print('your already at max hp')
                        return
                    else:
                        currentplayerhp += 10
                        print('the flame warden retaliates with an attack.')
                        currentplayerhp -= 8
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the minor flame for a brief moment')
                    print('would you like to heal before the minor flame attacks')
                    myanswer = input()
                    if myanswer == 'yes':
                        currentplayerhp += 10
                        print('your hp ' + str(currentplayerhp))
                    else:
                        continue
                else:
                    currentplayerhp -= 5
                    print('your hp ' + str(currentplayerhp))
    print('you defeated the minor flame your heal ability has increased from 10'
          ' to 15 points')
    print('will you continue down the hall?')
    myanswer = input()
    if myanswer == 'yes':
        print('you run into a medium flame, it takes an offensive stance')
        currentflamehp = beastiary['medium_flame']
        while currentflamehp > 0:
            print('you can fight, heal, or run what will you do')
            myact = input()
            if myact == 'fight':
                currentflamehp -= 30
                print('medium flame hp ' + str(currentflamehp))
                print('the medium flame attacks')
                currentplayerhp -= 6
                print('Your hp ' + str(currentplayerhp))
                if currentplayerhp < 0:
                    print('your journey has come to an end')
                    quit()
            elif myact == 'heal':
                if currentplayerhp >= playerhp[level_2]:
                    print('your already at max hp')
                    return
                else:
                    currentplayerhp += 15
                    print('the flame warden retaliates with an attack.')
                    currentplayerhp -= 8
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('alas you have died by the flame')
                        quit()
            elif myact == 'run':
                print('you escape for a brief moment.')
                print('would you like to heal?')
                myanswer = input()
                if myanswer == "yes":
                    currentplayerhp += 15
                    print('Your hp ' + str(currentplayerhp))
                    print('the medium flame pursues.')
                else:
                    print('the medium flame catches you the battle'
                          'resumes')
            else:
                print('The medium flame attacks')
                currentplayerhp -= 6
                print('Your Hp ' + str(currentplayerhp))
                if currentplayerhp < 0:
                    print('your journey has come to an end')
                    quit()
    else:
        print('you turn back leaving this world to burn.')
        quit()
    print('you have defeated the medium flame gaining a level.')
    currentplayerhp = playerhp['level_3']
    print('would you like to continue down the hall')
    myanswer = input()
    if myanswer == 'yes':
        print('You approach a Major flame will you approach?')
        myanswer = input()
        if myanswer == 'yes':
            currentflamehp = beastiary['major_flame']
            while currentflamehp > 0:
                print('The Major flame attacks you can fight, run or heal.')
                myact = input()
                if myact == "fight":
                    currentflamehp -= 35
                    print('Major flame HP ' + str(currentflamehp))
                    currentplayerhp -= 7
                    print('Your Hp' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
                elif myact == 'heal':
                    if currentplayerhp >= playerhp[level_3]:
                        print('your already at max hp')
                        return
                    else:
                        currentplayerhp += 10
                        print('the flame warden retaliates with an attack.')
                        currentplayerhp -= 8
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == "run":
                    print('You escape from the Major flame.')
                    print('would you like to heal?')
                    myanswer = input()
                    if myanswer == 'yes':
                        currentplayerhp += 15
                        print('your Hp ' + str(currentplayerhp))
                        print('The major flame pursues.')
                    else:
                        print('The Major flame pursues.')
                else:
                    print("the major flame attacks.")
                    currentplayerhp -= 7
                    print('Your Hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
    else:
        print('Your journey has come to an end thanks for playing'
        'now deleting all progress.')
        quit()
    print('You have gained a level your healing has increased '
          'from 15 to 20')
    currentplayerhp = playerhp['level_4']
    print('The hall splits here you can go right or left.')
    print('what will you do?')
    myanswer = input()
    if myanswer == "right":
        print('you run into a group of major flames')
        currentflamehp = beastiary['major_flame']
        currentflamehp1 = beastiary['major_flame']
        while (currentflamehp, currentflamehp1) > 0:
            myact = input()
            if myact == 'fight':
                print('The left or right major flame')
                mymove = input()
                if mymove == 'right major flame':
                    if currentflamehp <= 0:
                        print('The right major flame is dead attack the other'
                        'one')
                    currentflamehp -= 35
                    print('Rmajor flame ' + str(currentflamehp))
                    currentplayerhp -= 14
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
                elif mymove == 'left major flame':
                    if currentflamehp1 <= 0:
                        print('The left major flame is dead attack the other'
                        'one jeez')
                        return
                    currentflamehp1 -= 35
                    print('Lmajor flame ' + str(currentflamehp1))
                    currentplayerhp -= 14
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
                else:
                    print('you got to choose between \'left major flame\''
                          ' or \'right major flame\'')
            elif myact == 'heal':
                if currentplayerhp >= playerhp[level_4]:
                    print('your already at max hp')
                    return
                else:
                    currentplayerhp += 20
                    print('the flame warden retaliates with an attack.')
                    currentplayerhp -= 8
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('alas you have died by the flame')
                        quit()
            elif myact == 'run':
                print('you escape the major flames')
                print('would you like to heal?')
                myanswer =input()
                if myanswer == 'yes':
                    currentplayerhp += 20
                    print('Your hp ' + str(currentplayerhp))
                    print('The major flames pursues')
                else:
                    print('The major flames pursues')
            else:
                currentplayerhp -= 14
                print('Your Hp ' + str(currentplayerhp))
                if currentplayerhp < 0:
                    print('your journey has come to an end')
                    quit()
    print('You have gained a level you are now level 5 and can heal for 25'
    'points, and deal 40 dmg')
    currentplayerhp = playerhp[level_5]
    print('will you continue down the hallway?')
    myanswer = input()
    if myanswer = "yes":
        print('you come across a fire walker it seems like it hasn\'t noticed you')
        currentflamehp = beastiary[fire_walker]
        print('will you attack it and deal 2x dmg? Or will you sneak by it?')
        myanswer = input()
        if myanswer == 'attack':
            currentflamehp -= 80
            print(currentflamehp)
            while currentflamehp > 0:
                print('you can fight, run, or heal what shall you do')
                myact = input()
                if myact == 'fight':
                    currentflamehp -= 40
                    print('Fire walker hp' + str(currentflamehp) + 'it attacks.')
                    currentplayerhp -= 8
                    print('Your hp' + str(currentplayerhp))
                elif myact == 'heal':
                    if currentplayerhp >= playerhp[level_4]:
                        print('your already at max hp')
                        return
                    else:
                        currentplayerhp += 25
                        print('the flame warden retaliates with an attack.')
                        currentplayerhp -= 8
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the fire walker.')
                    print('would you like to heal?')
                    myanswer =input()
                    if myanswer == 'yes':
                        currentplayerhp += 25
                        print('Your hp ' + str(currentplayerhp))
                        print('The fire walker pursues.')
                    else:
                        print('The fire walker pursues.')
                else:
                    currentplayerhp -= 8
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
        elif myanswer == 'sneak':
            print('you sneak by the fire walker.')
            print('or so you thought too bad your not a ninja.')
            while currentflamehp > 0:
                print('you can fight, run, or heal what shall you do')
                myact = input()
                if myact == 'fight':
                    currentflamehp -= 40
                    print('Fire walker hp' + str(currentflamehp) + 'it attacks.')
                    currentplayerhp -= 8
                    print('Your hp' + str(currentplayerhp))
                elif myact == 'heal':
                    if currentplayerhp >= playerhp[level_4]:
                        print('your already at max hp')
                        return
                    else:
                        currentplayerhp += 25
                        print('the flame warden retaliates with an attack.')
                        currentplayerhp -= 8
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the fire walker.')
                    print('would you like to heal?')
                    myanswer =input()
                    if myanswer == 'yes':
                        currentplayerhp += 25
                        print('Your hp ' + str(currentplayerhp))
                        print('The fire walker pursues.')
                    else:
                        print('The fire walker pursues.')
                else:
                    currentplayerhp -= 8
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
        else:
            while currentflamehp > 0:
                print('you can fight, run, or heal what shall you do')
                myact = input()
                if myact == 'fight':
                    currentflamehp -= 40
                    print('Fire walker hp' + str(currentflamehp) + 'it attacks.')
                    currentplayerhp -= 8
                    print('Your hp' + str(currentplayerhp))
                elif myact == 'heal':
                    if currentplayerhp >= playerhp[level_4]:
                        print('your already at max hp')
                        return
                    else:
                        currentplayerhp += 25
                        print('the flame warden retaliates with an attack.')
                        currentplayerhp -= 8
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the fire walker.')
                    print('would you like to heal?')
                    myanswer =input()
                    if myanswer == 'yes':
                        currentplayerhp += 25
                        print('Your hp ' + str(currentplayerhp))
                        print('The fire walker pursues.')
                    else:
                        print('The fire walker pursues.')
                else:
                    currentplayerhp -= 8
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
