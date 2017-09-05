from Fire_game.Flame_world.Fire_world_main.actions import Actions
from Fire_game.Flame_world.Fire_world_main.player import Player
import copy
actions = Actions()
player = Player()


def game_loop(stage: str, player_obj: Player):
    global actions
    global player

    player = copy.deepcopy(player_obj)

    actions.do_action(stage, player)


def env_setup():
    global actions
    global player
    player.player_new()
    actions.set_game_loop(game_loop)


def main():
    global player
    env_setup()
    game_loop('door', player)


if __name__ == '__main__':
    main()
