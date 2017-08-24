from Flame_world.Fire_world_main import statements

from Flame_world.Fire_world_main.interact import exit_game
from Flame_world.Fire_world_main.interact import get_player_input
from Flame_world.Fire_world_main.interact import player_print

from Flame_world.Fire_world_main.monsters import flame
from Flame_world.Fire_world_main.monsters import flamewarden
from Flame_world.Fire_world_main.monsters import mediumflame

from Flame_world.Fire_world_main.player import Player

from typing import Callable


class GameActions(object):
    def __init__(self) -> None:
        self._game_loop = None

    def set_game_loop(self, game_loop: Callable) -> None:
        self._game_loop = game_loop


class ActionsMonsters(GameActions):
    def __init__(self):
        GameActions.__init__(self)
        self.flame = flame.Flame()
        self.flame_warden = flamewarden.FlameWarden()

    def do_fight_flame(self, player: Player) -> None:
        self.flame.set_game_loop(self._game_loop)
        self.flame.start_fight(player)

    def do_fight_flame_warden(self, player: Player) -> None:
        self.flame_warden.set_game_loop(self._game_loop)
        self.flame_warden.start_fight(player)

    def do_fight_medium_flame(self, player: Player)-> None:
        self.medium_flame.set_game_loop(self._game_loop)
        self.medium_flame.start_fight(player)


class ActionsMovements(GameActions):
    def __init__(self):
        GameActions.__init__(self)

    def do_game_door(self, player: Player) -> None:
        pa = get_player_input(statements.door_enter_question,
                              statements.door_enter_answers)
        if pa.lower() == 'no':
            exit_game(statements.exit_too_bad)
        else:
            self._game_loop('hallway', player)

    def do_game_flame_fork(self, player: Player) -> None:
        player_print(statements.fire_fork_statement)
        pa = get_player_input(statements.fire_fork_question,
                              statements.fire_fork_answers)
        if pa.lower() == 'left':
            self._game_loop('flame_fork_left', player)
        else:
            self._game_loop('flame_fork_right', player)

    def do_game_flame_fork_left(self, player: Player) -> None:
        player_print(statements.fire_fork_left_statement)
        pa = get_player_input(statements.fire_fork_left_question,
                              statements.fire_fork_left_answers)
        if pa.lower == 'yes':
            self._game_loop('medium_flame', player)
        else:
            exit_game(statements.fire_fork_left_answers_no)

    def do_game_hallway_continue(self, player: Player)-> None:
        player_print(statements.hallway_continue_statement)
        pa = get_player_input(statements.hallway_continue_question,
                              statements.hallway_continue_answers)
        if pa.lower() == 'yes':
            self._game_loop('major_flame', player)
        else:
            exit_game(statements.hallway_continue_answers_no)

    def do_game_flame_fork_right(self, player: Player) -> None:
        player_print(statements.fire_fork_right_statement)
        pa = get_player_input(statements.fire_fork_right_question,
                              statements.hallway_fire_answers)
        if pa.lower() == 'yes':
            self._game_loop('flame_warden', player)
        else:
            self._game_loop('fire_fork_left_return', player)

    def do_game_flame_fork_return(self, player: Player) -> None:
        player_print(statements.fire_fork_left_return)
        self._game_loop('flame_fork_left', player)

    def do_game_hallway(self, player: Player) -> None:
        player_print("{0}".format(statements.hallway_fire))
        pa = get_player_input(statements.hallway_fire_question,
                              statements.hallway_fire_answers)
        if pa.lower() == 'no':
            exit_game(statements.hallway_fire_answers_no)
        else:
            self._game_loop('fight_flame_monster', player)


class Actions(object):
    def __init__(self) -> None:
        self._game_loop = None
        self._monsters = ActionsMonsters()
        self._movements = ActionsMovements()
        self._map = dict()
        self._build_map()

    def _build_map(self) -> None:
        self._map['door'] = self._movements.do_game_door
        self._map['hallway'] = self._movements.do_game_hallway
        self._map['fight_flame_monster'] = self._monsters.do_fight_flame
        self._map['after_flame_fork'] = self._movements.do_game_flame_fork
        self._map['flame_fork_left'] = self._movements.do_game_flame_fork_left
        self._map['flame_fork_right'] = \
            self._movements.do_game_flame_fork_right
        self._map['fire_fork_left_return'] = \
            self._movements.do_game_flame_fork_return
        self._map['flame_warden'] = self._monsters.do_fight_flame_warden

    def do_action(self, action: str, player: Player) -> None:
        if action in self._map:
            self._map[action](player)
        else:
            raise ValueError("Unsupported Action: {0}".format(action))

    def set_game_loop(self, game_loop: Callable) -> None:
        self._game_loop = game_loop
        self._monsters.set_game_loop(game_loop)
        self._movements.set_game_loop(game_loop)
