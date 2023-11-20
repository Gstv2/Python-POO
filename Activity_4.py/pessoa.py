from datetime import datetime

class Pessoa:

  def __init__(self, n, dn, a):
    self._nome = n
    self._data_nascimento = dn
    self._altura = a
 
  
  def imprimir_dados(self):
    print("Nome:", self._nome, "\nData de Nascimento:" , self._data_nascimento, "\nAltura:", self._altura)
 

  def calcular_idade(self):
    ano_data_atual = datetime.today().year
     
    partes_data_nascimento = self._data_nascimento.split("/")
    ano_nascimento = partes_data_nascimento[2]
     
    anos = ano_data_atual - int(ano_nascimento)
    print("A pessoa tem", anos, "anos.")