from televisao import Televisao

class Controle_remoto:
    def __init__(self):
        self.t = Televisao()

    def aumentarV(self):
        if self.t.volume < 60.0:
            self.t.volume += 1.0
        else:
            print('Volume no máximo')

    def diminuirV(self):
        if self.t.volume > 1.0:
            self.t.volume -= 1.0
        else:
            print('Volume no mínimo')

    def canalE(self):
        print('Changing channel')

    def canalavolume(self):
        print(f'TV: {self.t}')


