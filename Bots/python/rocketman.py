from bot_interface import *

class RocketMan(BotBase):

    def process(self, gamestate):
        
        if (gamestate.tick < 30):
            # vai pra tras no começo
            return Action(-0.2, 0, 0, 1)

        motor1 = 0
        motorDaFrente = 0.0
        motorDeTras = 0.0
        forca = 0.2
        alterna = 1
        
        if ((gamestate.tick//10)%2):
            if (gamestate.tick//5)%2:
                alterna = 1
            else:
                alterna = 0

            if alterna==1:
                motorDaFrente = -1*forca
                motorDeTras = forca
            else:
                motorDaFrente = -2*forca
                motorDeTras = 2*forca
        
        else:
            if (gamestate.tick//5)%2:
                alterna = 1
            else:
                alterna = 0

            if alterna==1:
                motorDaFrente = 2*forca
                motorDeTras = -2*forca
            else:
                motorDaFrente = 1*forca
                motorDeTras = -1*forca
        
        return Action(motor1, motorDaFrente, motorDeTras, 1)


GameState(RocketMan()).connect()
