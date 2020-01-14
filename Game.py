import Utils
from Player import Player


class Game:
    spaces = Utils.import_spaces()
    properties = Utils.import_properties()

    def __init__(self, pcount):
        self.players = []
        for x in range(0, pcount):
            self.players.append(Player(x))

    def play_game(self, rounds):
        for unused in range(rounds):
            for player in self.players:
                # todo: figure out how to handle a player taking a turn
                pass
