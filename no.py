# coding: UTF-8

import collections


DisTri = collections.namedtuple('TRIA', ['p1', 'p2', 'p3'])

TAMANHOS = {
    'M1': DisTri(100, 200, 250),
    'M2': DisTri(100, 200, 300),
    'M3': DisTri(250, 400, 450),
    'M4': DisTri(1500, 2500, 3000),
    'M5': DisTri(1500, 2100, 2800),
    'M6': DisTri(400, 550, 800),
    'M7': DisTri(2000, 3000, 3500),
    'M8': DisTri(1800, 2000, 2300),
    'M9': DisTri(1500, 2100, 2800),
}



class Trafego(object):
    def __init__(self, estado, probablidade=None, tamanho=None):
        """  """
        self.estado = estado
        if tamanho and not isinstance(tamanho, DisTri):
            raise Exception('O tamanho deve ser um tipo Ponto')

        self.tamanho = tamanho

        if probablidade and not(probablidade >= 0 and probablidade <= 1.0):
            raise Exception('O valor da probablidade está fora do intervalo válido')

        self.probabilidade = probablidade

    def __repr__(self):
        return '%s [%s, %s]' % (
            self.estado.__class__.__name__,
            self.probabilidade,
            self.tamanho
        )

