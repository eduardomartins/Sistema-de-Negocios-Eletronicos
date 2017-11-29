# coding: utf-8
from no import No


class Lan(No):
    def __init__(self, probablidade=None, tamanho=None, velocidade=100, capacidade=0.8):
        super(Lan, self).__init__(probablidade=probablidade, tamanho=tamanho)
        self.velocidade = velocidade
        self.capaciade = capacidade

    def calcular(self):
        return self.velocidade


class ServidorAplicacao(No):
    def __init__(self, tempo_min, tempo_max, probablidade=None, tamanho=None):
        super(ServidorAplicacao, self).__init__(probablidade=probablidade, tamanho=tamanho)
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max

    def calcular(self):
        return self.velocidade


class ServidorWeb(No):
    def __init__(self, tempo_min, tempo_max, probablidade=None, tamanho=None):
        super(ServidorWeb, self).__init__(probablidade=probablidade, tamanho=tamanho)
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max

    def calcular(self):
        return self.velocidade


class ServidorBancoDados(No):
    def __init__(self, tempo_min, tempo_max, probablidade=None, tamanho=None):
        super(ServidorWeb, self).__init__(probablidade=probablidade, tamanho=tamanho)
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max

    def calcular(self):
        return self.velocidade