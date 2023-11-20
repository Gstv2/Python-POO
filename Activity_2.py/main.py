from controleremoto import Controle_remoto

controle = Controle_remoto()

for i in range(65):
    controle.aumentarV()

for i in range(1):
    controle.diminuirV()

for i in range(50):
    controle.canalD()

for i in range(30):
    controle.canalE()

controle.canalavolume()
