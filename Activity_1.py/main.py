from alarme import Alarme
from tarefa import Tarefa
from usuario import Usuario

u = Usuario(9772, "Gustavo nery", "Apollo12")
print(u.nome)
print(u.tarefas)

u.criarTarefa("Preparar insurreição!", "14:00","18:00",u)
u.criarTarefa("Preparar cura!", "14:00","18:00",u)

#print(u.tarefas)
print(u.tarefas[0].descriçao)

ta = Tarefa("Preparar insurreição!", "14:00","18:00",u)

#print(ta.alarme)
ta.criarAlarme()
ta.criarAlarme()
ta.alarme[1].redefinirAlarme()

for a in ta.alarme:
   a.exibirAlarme()

ta.excluirAlarme(0)

for a in ta.alarme:
  a.exibirAlarme()
