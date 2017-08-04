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
                    break
            else:
                print('the flame engulfs you')
                break
    print('you have gained a level you can now use the heal command in battle.')
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
                while currentflamehp > 0
                    myact = input()
                    if myact == 'fight':
                        currentflamehp -= 25
                        print('flame warden' + str(currentflamehp))
                        currentplayerhp -= 8
                        print('you' + str(currentplayerhp))
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                    elif myact == 'heal'
                        currentplayerhp += 10
                        print('you' +str(currentplayerhp))
                        print('the flame warden retaliates with an attack.')
                        currentplayerhp -= 8
                        if currentplayerhp < 0:
                            print('alas you have died by the flame')
                            quit()
                    elif myact == 'run'
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
    elif mymove == 'left':
        print('you meet a minor flame will you approach?')
        myanswer = input()
        if myanswer == 'yes':
            currentflamehp = beastiary['minor_flame']
            while currentflamehp > 0