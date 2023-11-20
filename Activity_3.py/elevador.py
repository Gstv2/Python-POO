class Elevador:
  # Construtor
  def __init__(self, c, t):
    self.capacidade = c
    self.total_andar = t
    self.carga = 0
    self.andar_atual = 0
    self.sentido = False

  # Métodos
  def entrar(self):
    if (self.carga < self.capacidade):
      self.carga = self.carga+1
      print("Entrou um!")

  def sair(self):
    if (self.carga > 0):
      self.carga = self.carga-1
      print("Saiu um!")

  def subir(self):
    if (self.andar_atual < self.total_andar):
      self.andar_atual = self.andar_atual+1
      print("Subiu um andar!")

  def descer(self):
    if (self.andar_atual >0):
      self.andar_atual = self.andar_atual-1
      print("Desceu um andar!")

