class Televisao:
    def __init__(self, canal=0, volume=0.0):
        self.canal = canal
        self.volume = volume
        self.tudo = []

    def Dados(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def __str__(self):
        return f'Canal: {self.canal}, Volume: {self.volume}'