def _get_player_input(question: str) -> str:
    pl = input("\n{0}".format(question))
    if len(pl) < 1:
        return _get_player_input(question)
    return pl


def _get_player_input_acceptable(question: str,
                                 acceptable_answers: list) -> str:
    pl = input("\n{0}\n [{1}]: ".format(question,
                                        ','.join(acceptable_answers)))
    if len(pl) < 1:
        return _get_player_input_acceptable(question, acceptable_answers)
    if pl.lower() not in acceptable_answers:
        return _get_player_input_acceptable(question, acceptable_answers)
    return pl


def exit_game(statement: str) -> None:
    print("\n{0}".format(statement))
    raise SystemExit()


def get_player_input(question: str, acceptable_answers: [list, None]) -> str:
    if type(acceptable_answers) == list and len(acceptable_answers) > 0:
        return _get_player_input_acceptable(question, acceptable_answers)
    else:
        return _get_player_input(question)


def player_print(statement: str) -> None:
    print("\n{0}".format(statement))
