from bot_interface import *
from math import sqrt
from math import cos
from math import acos
from math import sin
from math import pi


def dis(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def ang2v(x1, y1, x2, y2):
    aux = (sqrt(x1**2 + y1**2)*sqrt(x2**2 + y2**2))
    if aux == 0:
        aux = 1
    return acos((x1*x2 + y1*y2) / aux)


class Calouros(BotBase):
    def process(self, gamestate):
        sf = 0
        sb = 0
        moto = 0

        if 10 < gamestate.tick < 30:
            moto = 1
        elif 30 < gamestate.tick < 50:
            moto = -1
        # elif 51 < gamestate.tick:
            # moto = -1
            # sb = 1
            # sf = -1
        # elif 51 < gamestate.tick < 70:
        #     sf = -1
        #     sb = 1

        vid = [gamestate.rocks[i] for i in gamestate.rocks]

        pedra = 0
        mi = 1000000000
        for i in range(len(vid)):
            dd = dis(self.posx, self.posy, vid[i].posx, vid[i].posy)
            dd -= self.radius + vid[i].radius
            if dd < mi:
                mi = dd
                pedra = i

        # gamestate.log((self.ang-270)%360)
        if mi < 5:
            ang = ((self.ang-270) % 360)/180*pi
            v1x = int(sin(ang))
            v1y = int(cos(ang))
            v2x = self.posx - vid[pedra].posx
            v2y = self.posy - vid[pedra].posy
            angdif = ang2v(v1x, v1y, v2x, v2y)

            # gamestate.log(ang)
            # gamestate.log(v1x)
            # gamestate.log(v1y)
            # gamestate.log(angdif)
            # gamestate.log(cos(angdif))
            # gamestate.log(sin(angdif))

            moto = sin(angdif)
            sf = cos(angdif)
            sb = cos(angdif)
        elif gamestate.tick > 51:
            moto = self.vely

        return Action(moto, sf, sb, 1)


GameState(Calouros()).connect()
