# coding: UTF-8

import time
from numpy.random import trangular


class Observable(object):
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

class Pacote(object):
    def __init__(self, id, tempo_inicial=0, tamanho=0):
        self.id = id
        self._tamanho = 0
        self.tempo_sis = 0
        self.tempo_fila = 0
        self.tempo_ocioso = 0
        self.tempo_inicial = tempo_inicial
    
    def set_tamanho(self, tamanho):
        self._tamanho = tamanho
     
    @properity
    def tamanho(self):
        return triangular(self._tamanho[0], self._tamanho[1], self._tamanho[2])
    
    def atualiza_tempo(self, tempo_sis=0, tempo_fila=0, tempo_ocioso=0):
        self.tempo_sis += tempo_sis
        self.tempo_fila += tempo_fila
        self.tempo_ocioso += tempo_ocioso

    @property
    def tempo_total(self):
        return self.tempo_fila + self.tempo_ocioso + self.tempo_sis

    @property
    def tempo(self):
        return self.tempo_total - self.tempo_inicial

    def __repr__(self):
        return "Pacote: %s | tempo(%s)" % (self.id, self.tempo)


class Cliente(Observable):
    pacotes_hora = 250
    
    def iniciar(self, pacotes=0, delay=0):
        for pac_id in range(self.pacotes_hora + pacotes):
            pacote = Pacote(pac_id)
            pacote.atualiza_tempo(tempo_sis=delay)
            self.update_observers(pacote)
