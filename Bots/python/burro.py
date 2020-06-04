from bot_interface import *
import math
from random import randint, choice


class Burro(BotBase):
    '''
    Burrobot só fica se mexendo aleatoriamente e é isto
    '''

    def process(self, gamestate):
        if(gamestate.tick < 20):
            if self.charge > 2:
                Action.SHOOT = Action(0, 0, 0, 0)
                Action.SHOOT = Action(0, 0, 0, 0)
                return Action(-0.2, -.2, -.2, 3)
            else:
                Action.SHOOT = Action(0, 0, 0, 0)
                Action.SHOOT = Action(0, 0, 0, 0)
                return Action(-0.2, -0.2, -0.2, 0)
        else:
            if gamestate.tick % 20:
                Action.SHOOT = Action(0, 0, 0, 0)
                Action.SHOOT = Action(0, 0, 0, 0)
                return Action(-0.2, randint(-1, 1), randint(-5, 5)/10, 0)
        Action.SHOOT = Action(0, 0, 0, 0)
        Action.SHOOT = Action(0, 0, 0, 0)
        return Action(-1, 0, 0, 0)


GameState(Burro()).connect()
