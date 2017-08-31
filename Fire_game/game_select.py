from Flame_world.core_game_infinite import core_game_infinite
from Flame_world.core_game import core_game


print('what game mode would you like to play?')
game=input('infinite or story')
if game == infinite:
    core_game_infinite
else:
    core_game
