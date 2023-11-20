from televisao import Televisao

class Controle_remoto:
    def __init__(self):
        self.t = Televisao()

    def aumentarV(self):
        if self.t.volume <= 60.0:
            self.t.volume += 1.0
        else:
            print('Volume no máximo')

    def diminuirV(self):
        if self.t.volume > 1.0:
            self.t.volume -= 1.0
        else:
            print('Volume no mínimo')

    def canalD(self):
        if self.t.canal <= 60:
            self.t.canal += 1
        else:
            print('Canal não existente')

    def canalE(self):
        if self.t.canal >= 1:
            self.t.canal -= 1
        else:
            print('Canal não existente')

    def canalavolume(self):
        print(f'TV: {self.t}')


