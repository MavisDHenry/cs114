from random import randint


playerhp = {'level_1': 100, 'level_2': 110, 'level_3': 120, 'level_4': 130,
            'level_5': 140, 'level_6': 150, 'level_7': 160, 'level_8': 170,
            'level_9': 180, 'level_10': 200, 'level_11': 210, 'level_12': 220,
            'level_13': 230, 'level_14': 240, 'level_15': 250}
flamehp = 200
currentflamehp = flamehp
currentplayerhp = playerhp['level_1']
beastiary = {'minor_flame': 200, 'medium_flame': 250, 'major_flame': 300,
             'fire_walker': 500, 'flame_warden': 700, 'flame_devil': 1000,
             'inferno_walker': 2000, 'inferno_warden': 4000,
             'inferno_devil': 6000}


def battle_action(level):
    base_dmg = 25
    dmg_per_level = 5

    total_dmg = randint(base_dmg , (dmg_per_level * level) + base_dmg)

    return total_dmg


def monster_attack(level):
    base_dmg = 4
    dmg_per_level = 1

    total_dmg = randint(base_dmg, (dmg_per_level * level) + base_dmg)

    return total_dmg


def heal_action (level):
    base_heal = 10
    heal_per_level = 5

    total_heal = randint(base_heal, (heal_per_level * level) + base_heal)

    return total_heal


def HP_barrier (level):
    base_barrier = 200
    barrier_per_level = 50

    total_barrier = randint(base_barrier, (barrier_per_level * level) + base_barrier)

    return total_barrier


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
                battle_action(1)
                currentflamehp -= battle_action(1)
                print('flame hp ' + str(currentflamehp))
                monster_attack(0)
                currentplayerhp -= monster_attack(0)
                print('Your hp ' + str(currentplayerhp))
                if currentplayerhp <= 0:
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
            print('you enter a room with a flame warden, '
                  'will you fight or run?')
            myact = input()
            if myact == 'fight':
                print('The flame warden attacks dealing 8 dmg.')
                currentplayerhp -= 8
                currentflamehp = beastiary['flame_warden']
                while currentflamehp > 0:
                    myact = input()
                    if myact == 'fight':
                        battle_action(2)
                        currentflamehp -= battle_action(2)
                        print('flame warden hp ' + str(currentflamehp))
                        monster_attack(7)
                        currentplayerhp -= monster_attack(7)
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp <= 0:
                            print('alas you have died by the flame')
                            quit()
                    elif myact == 'heal':
                        if currentplayerhp >= playerhp['level_2']:
                            print('your already at max hp')
                        else:
                            heal_action(1)
                            currentplayerhp += heal_action(1)
                            print('the flame warden retaliates with an attack.')
                            monster_attack(1)
                            currentplayerhp -= monster_attack(1)
                            print('your hp ' + str(currentplayerhp))
                            if currentplayerhp <= 0:
                                print('alas you have died by the flame')
                                quit()
                    elif myact == 'run':
                        print('you flee from the flame warden in terror '
                              'only to be caught by him moments later')
                        monster_attack(7)
                        currentplayerhp -= monster_attack(7)
                        print('you' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                    else:
                        monster_attack(7)
                        currentplayerhp -= monster_attack(7)
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                print('you have defeated the flame warden.')
                print('the game is now over good job '
                      'doing things the hard way.')
                quit()
            else:
                print('you run straight past the'
                      ' flame warden straight into the fire devil')
                myact = input()
                print('you have died to the true final boss play the '
                      'long route to actually stand a chance.')
                quit()
    elif mymove == 'left':
        print('you meet a minor flame will you approach?')
        myanswer = input()
        if myanswer == 'yes':
            currentflamehp = beastiary['minor_flame']
            while currentflamehp > 0:
                print(' you have engaged in battle with the minor flame '
                      'you can fight, run, or heal, what will you do?')
                myact =input()
                if myact == "fight":
                    battle_action(2)
                    currentflamehp -= battle_action(2)
                    print('minor flame ' + str(currentflamehp))
                    monster_attack(1)
                    currentplayerhp -= monster_attack(1)
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp <= 0:
                        print('alas brave adventurer you '
                              'have been incinerated.')
                        quit()
                elif myact == 'heal':
                    if currentplayerhp >= playerhp['level_2']:
                        print('your already at max hp')
                    else:
                        heal_action(1)
                        currentplayerhp += heal_action(1)
                        print('the minor flame retaliates with an attack.')
                        monster_attack(1)
                        currentplayerhp -= monster_attack(1)
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp <= 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the minor flame for a brief moment')
                    print('would you like to heal before the'
                          ' minor flame attacks')
                    myanswer = input()
                    if myanswer == 'yes':
                        heal_action(1)
                        currentplayerhp += heal_action(1)
                        print('your hp ' + str(currentplayerhp))
                    else:
                        continue
                else:
                    monster_attack(1)
                    currentplayerhp -= monster_attack(1)
                    print('your hp ' + str(currentplayerhp))
    else:
        print('You should have chosen a path instead of whatever you did, '
              'remember it is case sensitive always use lower case')
        print('the world around grows hotter you have burned to death due '
              'to your lack of movement')
        quit()
    print('you defeated the minor flame your heal ability has increased '
          'from 10 to 15 points')
    print('will you continue down the hall?')
    myanswer = input()
    if myanswer == 'yes':
        print('you run into a medium flame, it takes an offensive stance')
        currentflamehp = beastiary['medium_flame']
        while currentflamehp > 0:
            print('you can fight, heal, or run what will you do')
            myact = input()
            if myact == 'fight':
                battle_action(2)
                currentflamehp -= battle_action(2)
                print('medium flame hp ' + str(currentflamehp))
                print('the medium flame attacks')
                monster_attack(2)
                currentplayerhp -= monster_attack(2)
                print('Your hp ' + str(currentplayerhp))
                if currentplayerhp <= 0:
                    print('your journey has come to an end')
                    quit()
            elif myact == 'heal':
                if currentplayerhp >= playerhp['level_2']:
                    print('your already at max hp')
                else:
                    heal_action(2)
                    currentplayerhp += heal_action(2)
                    print('the medium flame retaliates with an attack.')
                    currentplayerhp -= 6
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('alas you have died by the flame')
                        quit()
            elif myact == 'run':
                print('you escape for a brief moment.')
                print('would you like to heal?')
                myanswer = input()
                if myanswer == "yes":
                    heal_action(2)
                    currentplayerhp += heal_action(2)
                    print('Your hp ' + str(currentplayerhp))
                    print('the medium flame pursues.')
                else:
                    print('the medium flame catches you the battle'
                          'resumes')
            else:
                print('The medium flame attacks')
                monster_attack(2)
                currentplayerhp -= monster_attack(2)
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
                    battle_action(3)
                    currentflamehp -= battle_action(3)
                    print('Major flame HP ' + str(currentflamehp))
                    monster_attack(3)
                    currentplayerhp -= monster_attack(3)
                    print('Your Hp' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
                elif myact == 'heal':
                    if currentplayerhp >= playerhp['level_3']:
                        print('your already at max hp')
                    else:
                        heal_action(2)
                        currentplayerhp += heal_action(2)
                        print('the major flame retaliates with an attack.')
                        monster_attack(3)
                        currentplayerhp -= monster_attack(3)
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == "run":
                    print('You escape from the Major flame.')
                    print('would you like to heal?')
                    myanswer = input()
                    if myanswer == 'yes':
                        heal_action(2)
                        currentplayerhp += heal_action(2)
                        print('your Hp ' + str(currentplayerhp))
                        print('The major flame pursues.')
                    else:
                        print('The Major flame pursues.')
                else:
                    print("the major flame attacks.")
                    monster_attack(3)
                    currentplayerhp -= monster_attack(3)
                    print('Your Hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
    else:
        print('Your journey has come to an end thanks for playing '
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
        while (currentflamehp + currentflamehp1) > 0:
            print('you can fight, run or heal.')
            myact = input()
            if myact == 'fight':
                print('The left or right major flame')
                mymove = input()
                if mymove == 'right':
                    if currentflamehp <= 0:
                        print('The right major flame is dead attack the other'
                              ' one')
                    battle_action(4)
                    currentflamehp -= battle_action(4)
                    if currentflamehp < 0:
                        currentflamehp = 0
                    print('major flame hp ' + str(currentflamehp))
                    monster_attack(3)
                    currentplayerhp -= monster_attack(3)
                    monster_attack(3)
                    currentplayerhp -= monster_attack(3)
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
                elif mymove == 'left':
                    if currentflamehp1 <= 0:
                        print('The left major flame is dead attack the other '
                              'one jeez')
                    battle_action(4)
                    currentflamehp1 -= battle_action(4)
                    if currentflamehp1 < 0:
                        currentflamehp1 = 0
                    print('Lmajor flame ' + str(currentflamehp1))
                    monster_attack(3)
                    currentplayerhp -= monster_attack(3)
                    monster_attack(3)
                    currentplayerhp -= monster_attack(3)
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
                else:
                    print('you got to choose between \'left\' major flame'
                          ' or \'right\' major flame)
            elif myact == 'heal':
                if currentplayerhp >= playerhp['level_4']:
                    print('your already at max hp')
                else:
                    heal_action(3)
                    currentplayerhp += heal_action(3)
                    print('the major flame retaliates with an attack.')
                    monster_attack(3)
                    currentplayerhp -=monster_attack(3)
                    monster_attack(3)
                    currentplayerhp-= monster_attack(3)
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('alas you have died by the flame')
                        quit()
            elif myact == 'run':
                print('you escape the major flames')
                print('would you like to heal?')
                myanswer =input()
                if myanswer == 'yes':
                    heal_action(3)
                    currentplayerhp += heal_action(3)
                    print('Your hp ' + str(currentplayerhp))
                    print('The major flames pursues')
                else:
                    print('The major flames pursues')
            else:
                monster_attack(3)
                currentplayerhp -= monster_attack(3)
                monster_attack(3)
                currentplayerhp -= monster_attack(3)
                print('Your Hp ' + str(currentplayerhp))
                if currentplayerhp < 0:
                    print('your journey has come to an end')
                    quit()
    elif myanswer == 'left':
        print('you come to the entrance into the furnace.')
        print('you feel immense heat coming from beyond the door.')
        print('will you go in or turn back?')
        myanswer = input()
        if myanswer == 'go in':
            print('you enter the room only to find an Inferno warden')
            currentflamehp = beastiary['inferno_warden']
            print('the air is so hot you begin to burn.')
            currentplayerhp -= 5
            while currentflamehp > 0:
                print('you can fight or heal the run command has been burned')
                myact = input()
                if myact == 'fight':
                    battle_action(4)
                    currentflamehp -= battle_action(4)
                    print('Inferno warden HP ' +str(currentflamehp))
                    monster_attack(20)
                    currentplayerhp -= monster_attack(20)
                    print('Your Hp ' + str(currentplayerhp) + 'the burning '
                                                              'damages you')
                    currentplayerhp -= 5
                    print('your Hp ' + str(currentplayerhp))
                    if currentplayerhp <= 0:
                        print('you have died leaving nothing but ash behind')
                        quit()
                elif myact == 'heal':
                    heal_action(4)
                    currentplayerhp += heal_action(4)
                    monster_attack(20)
                    currentplayerhp -= monster_attack(20)
                    currentplayerhp -= 5
                    print('Your HP ' + str(currentplayerhp))
                    if currentplayerhp <= 0:
                        print('you have failed to live only fire remains')
                        quit()
                else:
                    print('you can fight or heal only')
            if currentflamehp <= 0:
                print('you have defeated the Inferno warden but at the cost'
                ' of your sword unable to continue you head back only to be'
                ' consumed by the flame.')
                quit()
        else:
            print('you turn back and leave the last thing you hear is'
            ' <loud ringing noise>')
            quit()
    print('You have gained a level you are now level 5 and can heal for 25 '
          'points, and deal 40 dmg')
    currentplayerhp = playerhp['level_5']
    print('will you continue down the hallway?')
    myanswer = input()
    if myanswer == "yes":
        print('you come across a fire walker it seems like it hasn\'t '
              'noticed you')
        currentflamehp = beastiary['fire_walker']
        print('will you attack it and deal 2x dmg? Or will you sneak by it?')
        myanswer = input()
        if myanswer == 'attack':
            battle_action(5)
            currentflamehp -= (battle_action(5) * 2)
            print(currentflamehp)
            while currentflamehp > 0:
                print('you can fight, run, or heal what shall you do')
                myact = input()
                if myact == 'fight':
                    battle_action(5)
                    currentflamehp -= battle_action(5)
                    print('Fire walker hp ' + str(currentflamehp) +
                          ' it attacks.')
                    monster_attack(4)
                    currentplayerhp -= monster_attack(4)
                    print('Your hp' + str(currentplayerhp))
                elif myact == 'heal':
                    if currentplayerhp >= playerhp['level_5']:
                        print('your already at max hp')
                    else:
                        heal_action(4)
                        currentplayerhp += heal_action(4)
                        print('the fire walker retaliates with an attack.')
                        monster_attack(4)
                        currentplayerhp -= monster_attack(4)
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the fire walker.')
                    print('would you like to heal?')
                    myanswer =input()
                    if myanswer == 'yes':
                        heal_action(4)
                        currentplayerhp += heal_action(4)
                        print('Your hp ' + str(currentplayerhp))
                        print('The fire walker pursues.')
                    else:
                        print('The fire walker pursues.')
                else:
                    monster_attack(4)
                    currentplayerhp -= monster_attack(4)
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
                    battle_action(5)
                    currentflamehp -= battle_action(5)
                    print('Fire walker hp' + str(currentflamehp) +
                          'it attacks.')
                    monster_attack(4)
                    currentplayerhp -= monster_attack(4)
                    print('Your hp' + str(currentplayerhp))
                elif myact == 'heal':
                    if currentplayerhp >= playerhp['level_5']:
                        print('your already at max hp')
                    else:
                        heal_action(4)
                        currentplayerhp += heal_action(4)
                        print('the fire walker retaliates with an attack.')
                        monster_attack(4)
                        currentplayerhp -= monster_attack(4)
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the fire walker.')
                    print('would you like to heal?')
                    myanswer =input()
                    if myanswer == 'yes':
                        heal_action(4)
                        currentplayerhp += 25
                        print('Your hp ' + str(currentplayerhp))
                        print('The fire walker pursues.')
                    else:
                        print('The fire walker pursues.')
                else:
                    monster_attack(4)
                    currentplayerhp -= monster_attack(4)
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('your journey has come to an end')
                        quit()
        else:
            while currentflamehp > 0:
                print('you can fight, run, or heal what shall you do')
                myact = input()
                if myact == 'fight':
                    battle_action(5)
                    currentflamehp -= battle_action(5)
                    print('Fire walker hp' + str(currentflamehp) +
                          'it attacks.')
                    monster_attack(4)
                    currentplayerhp -= monster_attack(4)
                    print('Your hp' + str(currentplayerhp))
                elif myact == 'heal':
                    if currentplayerhp >= playerhp['level_4']:
                        print('your already at max hp')
                    else:
                        heal_action(4)
                        currentplayerhp += heal_action(4)
                        print('the fire walker retaliates with an attack.')
                        monster_attack(4)
                        currentplayerhp -= monster_attack(4)
                        print('your hp ' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                elif myact == 'run':
                    print('you escape the fire walker.')
                    print('would you like to heal?')
                    myanswer =input()
                    if myanswer == 'yes':
                        heal_action(4)
                        currentplayerhp += heal_action(4)
                        print('Your hp ' + str(currentplayerhp))
                        print('The fire walker pursues.')
                    else:
                        print('The fire walker pursues.')
                else:
                    currentplayerhp -= 8
                    print('Your hp ' + str(currentplayerhp))
                    if currentplayerhp <= 0:
                        print('your journey has come to an end')
                        quit()

    print('with the fire walker defeated you have gained a level you are now '
          'level 6 you have learned the barrier spell')
    print('will you continue down the path?')
    myanswer = input()
    if myanswer == 'yes':
        print('you go down the hall only to be met by a Flame warden it rushes'
        ' you, the battle comenses')
        barrier = 0
        currentflamehp = beastiary['flame_warden']
        while currentflamehp > 0:
            print('you can fight, run, barrier, or heal what shall you do')
            myact = input()
            if myact == 'fight':
                battle_action(6)
                currentflamehp -= battle_action(6)
                print('Flame warden hp' + str(currentflamehp) +
                      'it attacks.')
                monster_attack(5)
                currentplayerhp -= monster_attack(5)
                print('Your hp' + str(currentplayerhp))
            elif myact == 'heal':
                if currentplayerhp >= playerhp['level_4']:
                    print('your already at max hp')
                else:
                    heal_action(5)
                    currentplayerhp += heal_action(5)
                    print('the flame warden retaliates with an attack.')
                    monster_attack(5)
                    currentplayerhp -= monster_attack(5)
                    print('your hp ' + str(currentplayerhp))
                    if currentplayerhp < 0:
                        print('alas you have died by the flame')
                        quit()
            elif myact == 'run':
                print('you escape the flame warden.')
                print('would you like to heal?')
                myanswer =input()
                if myanswer == 'yes':
                    heal_action(5)
                    currentplayerhp += heal_action(5)
                    print('Your hp ' + str(currentplayerhp))
                    print('The flame warden pursues.')
            elif myact == 'barrier':
                if barrier == 1:
                    print('you\'ve used the max number of barriers.')
                    continue
                else:
                    print('you have shielded your hp')
                    HP_barrier(1)
                    currentplayerhp += HP_barrier(1)
                    print('your hp ' + str(currentplayerhp))
                    print('The flame warden attacks in retaliation')
                    monster_attack(5)
                    currentplayerhp -= monster_attack(5)
                    barrier += 1
                    print('your hp ' + str(currentplayerhp))
            else:
                print('you must have enter the wrong input try fight, run,'
                ' barrier, heal.')
    print('you have defeated the flame warden gaining a level you\'re now '
    'level 7 increasing your healing and barrier.')
    currentplayerhp = playerhp['level_7']
    print('the hall comes to a door here will you go through?')
    myanswer = input()
