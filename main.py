# coding: UTF-8
"""

"""
import time
import sys
from maquina import factory_maquina
from infra import Lan, ServidorBancoDados, ServidorWeb, ServidorAplicacao, Roteador
from cliente import Cliente

DELAY = 0.0005
VISITAS = 250


def main(argv=sys.argv):

    Interacao1 = factory_maquina('Interecao1')

    Interacao2 = factory_maquina('Interecao2')

    Interacao3 = factory_maquina('Interecao3')

    roteador = Roteador()

    interacao1 = Interacao1(roteador)
    interacao2 = Interacao2(roteador)
    interacao3 = Interacao3(roteador)

    interacao1.inicial\
        .add_proximo(ServidorWeb(100, 300))

    interacao2.inicial\
        .add_proximo(ServidorWeb(100, 300))\
        .add_proximo(ServidorAplicacao(10, 20))\
        .add_proximo(ServidorBancoDados(10, 20))\
        .add_proximo(ServidorAplicacao(10, 20))

    interacao3.inicial.add_proximo(ServidorWeb(100, 300))

    cliente = Cliente()

    cliente.register(interacao1)

    pacotes = 0
    if len(argv) > 1:
        pacotes = int(argv[1])


    cliente.iniciar(pacotes, delay=DELAY)

    return 0



if __name__ == '__main__':
    main()
