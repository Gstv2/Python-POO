from alarme import Alarme

class Tarefa:
    descriçao = '' # descriçao da tarefa
    horaI = '' # hora de inicio
    horaT = '' # hora de termino
    usuario = None  # usuario da tarefa
    alarme = []

    def __init__(self,d,hi,ht, u):
      self.descriçao = d # chamando a variavel 
      self.horaI = hi
      self.horaT = ht
      self.usuario = u
    
    def criarAlarme(self):
      at = Alarme()
      self.alarme.append(at)

    def excluirAlarme(self,i):
      self.alarme.pop(i)


      