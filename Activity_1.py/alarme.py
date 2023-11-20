class Alarme:
  codigo = 0
  horaA = '20'
  ativo = True

  def redefinirAlarme(self):
    self.horaA = '00:00:00'

  def exibirAlarme(self):
    print(self.horaA)
