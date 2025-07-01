
class Player():
    def __init__(self):
        self.score = 0
        self.name = None

    def receive_score(self, received_score):
        self.score = received_score

    def _get_name_for_player_from_input(self):
        pass

    def prompt_for_name(self) -> str:
        self.input_name = self._get_name_for_player_from_input()

        if self.input_name == "":
            raise InvalidPlayerNameException("Player name cannot be empty.")
        

        else:
            self.name = self.input_name


class InvalidPlayerNameException(Exception):
    """Exception raised when a player name is invalid."""
    pass
