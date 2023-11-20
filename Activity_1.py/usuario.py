from tarefa import Tarefa

class Usuario:
    nome = ''
    codigo = 0
    username = ''
    tarefas = []

    def __init__(self,c,n,u):
        self.codigo = c
        self.nome = n
        self.username = u

    def criarTarefa(self, d, hi, ht, u):
        t = Tarefa( d, hi, ht, u)
        self.tarefas.append(t)
    