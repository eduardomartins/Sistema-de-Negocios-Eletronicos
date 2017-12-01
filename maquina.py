# coding: UTF-8

from queue import Queue
from random import random
from threading import Thread, Condition, Lock
from abc import ABCMeta, abstractmethod


class Maquina(object):
    __metaclass__ = ABCMeta

    _iteracoes = []

    def __init__(self, inicio):

        self.inicial = inicio        
        self._iteracoes.append(self)

        
    @abstractmethod
    def update(self, pacote, *args, **kwargs):
        print(pacote)
        estado = self.inicial
        estado.add_pacote(pacote)
        print("# %s - Tamanho da Fila: %s" % (estado, estado._fila.qsize()))

        while(estado):

            estado = estado.proximo()



class Estado(Thread):
    def __init__(self, *args, **kwargs):
        super(Estado, self).__init__(*args, **kwargs)
        self._fila = Queue()
        self._processando = Lock()
        self._disponivel = Condition(self._processando)
        self.proximos = dict()



    def __setitem__(self, key, value):
        self.proximos[key] = value

    def __getitem__(self, item):
        return self.proximos[item]

    def add_pacote(self, pacote):
        self._fila.put(pacote)

    def proximo(self):

        teto = 0

        num = round(random(), 2)

        for key, value in self.proximos.items():
            teto += key.probabilidade

            if num <= teto:
                return self.proximos[key]

        return None

    def __iter__(self):
        return self.proximo()
    

    def __repr__(self):
        return self.__class__.__name__


    def executar(self, pacote, *args, **kwargs):
        pass

    
    def run(self,*args, **kwargs):
        print("Executanto %s ..." % self.__class__.__name__)

        while True:
            #print('##', self.is_alive())
            while not(self._fila.empty()):
                if self._disponivel:

                    self.executar(self._fila.get(), *args, **kwargs)
            #else:
                #self._disponivel.wait()

