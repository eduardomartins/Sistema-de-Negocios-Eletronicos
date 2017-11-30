# coding: UTF-8


import _thread as thread
from abc import ABCMeta, abstractmethod


class Maquina(object):
    __metaclass__ = ABCMeta

    _iteracoes = []

    def __init__(self, inicial):

        if not isinstance(inicial, Estado):
            raise Exception('Incial deve ser um estado')

        self.inicial = inicial

        self._thread = thread.start_new_thread(self.setup, (self.__class__.__name__,))

        self._iteracoes.append(self)

    def setup(self, *args, **kwargs):
        print(self._iteracoes, *args, *kwargs)

    @abstractmethod
    def update(self, pacote, *args, **kwargs):
        print(pacote)


    def __iter__(self):
        proximo = self.inicial
        while(proximo):
            yield proximo
            proximo = proximo.proximo



class Estado(object):
    proximos = set()
    disponivel = True
    
    def __init__(self, proximos):
        self.proximos += set(proximos)

    def __iter__(self):
        probabilidades = [proximo.probabilidade for proximo in self.proximos]
        teto = 0
        for ind, prob in enumerate(probabilidades):
            teto += prob
            if n <= prob:
                return proximos[ind] 
    
    def __repr__(self):
        return '%s [%s, %s]' % (
            self.__class__.__name__,
            self.probabilidade,
            self.tamanho
    )

    def executar(self, pacote):
        raise NotImplementedError

    def add_proximo(self, proximo):
        self.proximo.append(proximo)
        return self.proximo.estado




def factory_maquina(class_name):
    return type(class_name, (Maquina, ), {'_fila_espera'    : []})
