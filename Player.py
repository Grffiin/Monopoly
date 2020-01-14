import random


class Player:
    """Base class for players"""
    current_space = 0
    in_jail = False
    cash = 1500
    properties = []

    def __init__(self, pid):
        self.pid = pid

    def take_turn(self):
        while True:
            doubles = 0
            rolled = False
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)

            # were doubles rolled?
            if d1 == d2:
                doubles += 1
                rolled = True
                if doubles == 3:
                    self.in_jail = True
                    # todo: put player in jail space
                    pass

            self.current_space = ((d1 + d2 + self.current_space) % 40)
            # todo: handle landing on the current space
            if rolled:
                continue
            break



