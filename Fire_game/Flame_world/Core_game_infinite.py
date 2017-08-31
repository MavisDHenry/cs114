from Flame_world.Fire_world_infinite.actions import Actions
from Flame_world.Fire_world_infinite.player import Player

actions = Actions()
player = Player()


def game_loop(stage: str, player_obj: Player):
    global actions

    actions.do_action(stage, player_obj)


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
