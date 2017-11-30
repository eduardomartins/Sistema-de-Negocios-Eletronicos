# coding: utf-8
from no import No, TAMANHOS
from maquina import Estado



class Firewall(Estado):
    pass



class Roteador(Estado):
    pass



class Lan(Estado):
    def executar(self, pacote):
        pacote.atualiza_tempo(0.00015) # Adiciona 0,00015 seg



class ServidorAplicacao(Estado):
    def __init__(self, tempo_min, tempo_max, *args, **kwargs):
        super(ServidorAplicacao, self).__init__(*args, **kwargs)
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max



class ServidorWeb(No, Estado):
    def __init__(self, tempo_min, tempo_max, *args, **kwargs):
        super(ServidorWeb, self).__init__(*args, **kwargs)
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max



class ServidorBancoDados(No, Estado):
    def __init__(self, tempo_min, tempo_max, *args, **kwargs):
        super(ServidorBancoDados, self).__init__(*args, **kwargs)
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max

