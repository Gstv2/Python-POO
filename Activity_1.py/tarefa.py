from alarme import Alarme

class Tarefa:
    descriçao = '' # descriçao da tarefa
    horaI = '' # hora de inicio
    horaT = '' # hora de termino
    usuario = None  # usuario da tarefa
    alarmes = []

    def __init__(self, descricao, hora_inicio, hora_termino, usuario):
        self.descricao = descricao
        self.hora_inicio = hora_inicio
        self.hora_termino = hora_termino
        self.usuario = usuario
        self.alarmes = []

    def criarAlarme(self):
        alarme = Alarme()
        self.alarmes.append(alarme)

    def excluirAlarme(self, indice):
        if 0 <= indice < len(self.alarmes):
            self.alarmes.pop(indice)
        else:
            print("Índice inválido para exclusão de alarme.")

    def __str__(self):
        alarmes_str = "\n".join(str(alarme) for alarme in self.alarmes)
        return f"Descrição: {self.descricao}\nHora de Início: {self.hora_inicio}\nHora de Término: {self.hora_termino}\nUsuário: {self.usuario}\n"
    


      