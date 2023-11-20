from elevador import Elevador

e1 = Elevador(5, 10)

# print(e1.carga)

e1.entrar()
e1.entrar()
e1.subir()
# e1.subir()
# e1.sair()
e1.subir()
# e1.sair()
# e1.sair()
e1.entrar()
e1.entrar()
e1.entrar()
# e1.entrar()
# e1.descer()

print("Pessoas: %d" % e1.carga)
print("Andar: %d" % e1.andar_atual)
