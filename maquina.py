# coding: UTF-8

from queue import Queue
from threading import Thread
from abc import ABCMeta, abstractmethod


class Maquina(object):
    __metaclass__ = ABCMeta

    _iteracoes = []

    def __init__(self, inicio):

        if not isinstance(inicio, Estado):
            raise Exception('Incial deve ser um estado')

        self.inicial = inicio        
        self._iteracoes.append(self)

        
    @abstractmethod
    def update(self, pacote, *args, **kwargs):
        print(pacote)


    def __iter__(self):
        proximo = self.inicial
        for pro in proximo:
            yield pro
            



class Estado(Thread):
    def __init__(self, proximos, *args. *kwargs):
        super(Estado, self).__init__(*args, *kwargs)
        self._fila = Queue()
        self._disponivel = True
        self.proximos += set(proximos)

    def __iter__(self):
        probabilidades = [proximo.probabilidade for proximo in self.proximos]
        teto = 0
        for ind, prob in enumerate(probabilidades):
            teto += prob
            if n <= prob:
                return proximos[ind] 
    
    def __repr__(self):
        return self.__class__.__name__
 
    
    def executar(self, pacote):
        raise NotImplementedError

    def add_proximo(self, proximo):
        self.proximo.append(proximo)
        return self.proximo.estado
    
    def run(self, pacote, *args, **kwargs):
        print("Executanto...")
        
        if self.disponivel:
            self.executar(pacote, *args, **kwargs)
        else:
            self._fila.put(pacote)
            while self.disponivel and :
                self.executar(pacote, *args, **kwargs)
                
