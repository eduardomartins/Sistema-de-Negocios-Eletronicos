# coding: utf-8
from maquina import Estado


class Firewall(Estado):

    def executar(self, pacote, interacao):
        self._disponivel.acquire()

        if interacao == 2:
            pacote.atualiza_tempo(0.00015) # Adiciona 0,00015 seg
        if interacao == 3:
            pacote.atualiza_tempo(0.00015) # Adiciona 0,00015 seg

        self._disponivel.release()


class Roteador(Estado):

    def executar(self, pacote):
        self._disponivel.acquire()

        pacote.atualiza_tempo(tempo_sis=0.00015) # Adiciona 0,00015 seg

        self._disponivel.release()

        self._disponivel.notify_all()


class Lan(Estado):
    capacidade = 0.8 * 0.125 # 0.125 MB/s equivale e 100Mbps

    def executar(self,  pacote):
        self._disponivel.acquire()

        pacote.atualiza_tempo(tempo_sis=pacote.tamanho/self.capacidade)


class ServidorAplicacao(Estado):

    def executar(self, pacote, interacao):
        self._disponivel.acquire()

        capacidade = 1

        if interacao == 2:
            capacidade = 1.0/(60 - 40)
        
        if interacao == 3:
            capacidade = 1.0/(120 - 60)

        pacote.atualiza_tempo(tempo_sis=capacidade)

        self._disponivel.release()

class ServidorWeb(Estado):

    def executar(self, pacote, interacao, numero):
        self._disponivel.acquire()

        capacidade = 1

        if interacao == 1:
            capacidade = 1.0/(6 - 4)
    
        if interacao == 2:
            if numero == 2:
                capacidade = 1.0/(7 - 5)
            if numero == 5:
                capacidade = 1.0/(10 - 7)
        
        if interacao == 3:
            capacidade = 1.0/(9 - 12)
        
        pacote.atualiza_tempo(tempo_sis=capacidade)

        self._disponivel.release()

class ServidorBancoDados(Estado):

    def executar(self, pacote):
        self._disponivel.acquire()

        capacidade = 1.0/(60 - 40) + 1/(400 - 50)
        
        pacote.atualiza_tempo(tempo_sis=capacidade)

        self._disponivel.release()


