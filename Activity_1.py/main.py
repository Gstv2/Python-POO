from tarefa import Tarefa
from usuario import Usuario

u = Usuario(9772, "Gustavo nery", "Apollo12")
print(20*'-=')
print(u.nome)
print(u.tarefas)



u.criarTarefa("Preparar insurreição!", "14:00","18:00",u)
u.criarTarefa("Preparar cura!", "14:00","18:00",u)
u.criarTarefa("Preparar ressureição!", "14:00","18:00",u)
u.criarTarefa("Preparar veneno!", "14:00","18:00",u)



#print(u.tarefas)
print(20*'-=')
print('Descrição de alguns alarmes')
print(u.tarefas[3].descricao)
print(u.tarefas[2].descricao)



ta = Tarefa(u.tarefas[0].descricao,u.tarefas[0].hora_inicio,u.tarefas[0].hora_termino,u.nome)
ta1 = Tarefa(u.tarefas[1].descricao,u.tarefas[1].hora_inicio,u.tarefas[1].hora_termino,u.nome)
ta2= Tarefa(u.tarefas[2].descricao,u.tarefas[2].hora_inicio,u.tarefas[2].hora_termino,u.nome)
ta3 = Tarefa(u.tarefas[3].descricao,u.tarefas[3].hora_inicio,u.tarefas[3].hora_termino,u.nome)
#print(ta.alarme)
ta.criarAlarme()
ta1.criarAlarme()
ta2.criarAlarme()
ta3.criarAlarme()
ta.alarmes[0].redefinirAlarme()



print(20*'-=')
print('Demonstração da criação dos alarmes:')
for a in ta.alarmes:
   a.exibirAlarme()
for a1 in ta1.alarmes:
   a1.exibirAlarme()
for a2 in ta2.alarmes:
   a2.exibirAlarme()
for a3 in ta3.alarmes:
   a3.exibirAlarme()


print("excluindo alarme 2")
ta.excluirAlarme(0)
ta3.excluirAlarme(0)


print(20*'-=')
for a in ta.alarmes:
   a.exibirAlarme()
for a1 in ta1.alarmes:
   a1.exibirAlarme()
for a2 in ta2.alarmes:
   a2.exibirAlarme()
for a3 in ta3.alarmes:
   a3.exibirAlarme()


print(20*'-=')
print("observando um dos alarmes")
print(20*'-=')
print(ta)
print(20*'-=')
print("observando um dos alarmes")
print(20*'-=')
print(ta1)
print(20*'-=')
print("observando um dos alarmes")
print(20*'-=')
print(ta2)
print(20*'-=')
print("observando um dos alarmes")
print(20*'-=')
print(ta3)
