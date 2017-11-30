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
    proximo = None
    disponivel = True

    def __init__(self, link = None):
        self.link = link

    def __iter__(self):
        return self.proximo

    def executar(self, pacote):
        raise NotImplementedError

    def add_proximo(self, proximo):
        self.proximo = proximo
        return self.proximo




def factory_maquina(class_name):
    return type(class_name, (Maquina, ), {'_fila_espera'    : []})
