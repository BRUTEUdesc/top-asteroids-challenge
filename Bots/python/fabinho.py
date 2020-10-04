from bot_interface import *


class Fabinho(BotBase):
    '''
    Fabinho é o bot mais brabo da ala direita da Via Láctea
    Desenvolvido em conjunto pelo pessoal do @fablabjoinville
    tem como objetivo destruir tudo e todos (com sorte).

    Até o momento Fabinho consegue:
        Encontrar seus oponentes
        Calcular a sua distância está os oponentes
        Escolher quem é o oponente mais próximo
    '''

    def dist(self, another_ship):
        '''
        Função que espera como parâmetro uma nave.
        Seu retorno é a distância Euclidiana entre Fabinho e a nave
        '''
        x1, y1 = self.posx, self.posy
        x2, y2 = another_ship.posx, another_ship.posy
        dist = ((y2-y1)**2 + (x2-x1)**2) ** (1/2)
        return dist

    def process(self, gamestate):
        '''
        Função chamada a cada tick
        É espero como retorno uma Action
        '''
        dists = []
        ships = gamestate.ships
        for uid, ship in ships.items():
            if uid != self.uid:
                dist = self.dist(ship)
                dists.append([uid, dist])

        dists = sorted(dists, key=lambda x: x[1])
        uid_perto, dist_perto = dists[0]
        self.log(f'O cara mais perto é o {uid_perto} e esta a {dist_perto} ')

        if dist_perto < 45:
            return Action(-.2, -.1, .1, 3)

        return Action(0, 0, 0, 0)


GameState(Fabinho()).connect()
