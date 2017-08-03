playerhp = int(100)
flamehp = int(200)
currentflamehp = int(flamehp)
currentplayerhp = int(playerhp)
playeratt = int(currentflamehp - 25)
flameatt = int(currentplayerhp - 5)
print('hello your about to enter a world of burning or a building that\'s on '
      'fire')
print('your sword has turned into a torrent of water just in the shape of a'
      ' sword')
print('you start in a room with a door will you go through?')
myanswer = input()
if myanswer == 'yes':
    print('you walk through the door into a hallway that is covered in flame')
    print('will you approach the flame?')
    if myanswer == 'yes':
        print('The flame attacks')
        while int(currentflamehp) > 0:
            print('you can fight the flame, or run from the flame what'
                  ' will you do?')
            myact = input()
            if myact == "fight":
                playeratt
                currentflamehp = playeratt
                print(currentflamehp)
                flameatt
                currentplayerhp = flameatt
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
