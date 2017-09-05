from Fire_game.Flame_world import Core_game
from Fire_game.Flame_world import Core_game_infinite


print('what game mode would you like to play?')
game = input('infinite or story. ')
if game == 'infinite':
    Core_game_infinite.main()
elif game == "story":
    Core_game.main()
else:
    game = input('that\'s not what i asked... '
                 'unless you were trying to quit? ')
    if game == 'infinite':
        Core_game_infinite.main()
    elif game == "story":
        Core_game.main()
    else:
        quit()