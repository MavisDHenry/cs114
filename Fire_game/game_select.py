from Fire_game.Flame_world import Core_game
from Fire_game.Flame_world import Core_game_infinite


print('what game mode would you like to play?')
game = input('infinite or story. ')
if game == 'infinite':
    Core_game_infinite.main()
else:
    Core_game.main()
