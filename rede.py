# coding: UTF-8

import time
import _thread



class Rede(object):
    def __init__(self, componetes):
        self.componentes = componetes
        try:
            self._thread = _thread.start_new_thread(self.processar)
        except:
            Exception("Nao foi possível iniciar a thread")

    def processar(self):
        for comp in self.componentes:
            comp.delay()