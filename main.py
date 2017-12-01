# coding: UTF-8
"""

"""
import sys

import maquina
from maquina import Maquina
from cliente import Cliente
from fluxo import Fluxo
from infra import Lan, ServidorBancoDados, ServidorWeb, ServidorAplicacao, Roteador, Firewall


DELAY = 0.0005
VISITAS = 250


def main(argv=sys.argv):
   
    lan1 = Lan()
    lan1.start()

    lan2 = Lan()
    lan2.start()

    fw = Firewall()
    fw.start()

    rot = Roteador()
    rot.start()

    sw = ServidorWeb()
    sw.start()

    sa = ServidorAplicacao()
    sa.start()

    bd = ServidorBancoDados()
    bd.start()

    maquina = Maquina(rot)


    rot[Fluxo()] = lan1

    lan1[Fluxo()] = sw

    sw[Fluxo(0.95, 'M3')] = sa

    sa[Fluxo(0.2, 'M4')] = sw

    sa[Fluxo(0.8, 'M6')] = bd

    bd[Fluxo(1.0, 'M7')] = sa

    sa[Fluxo(1.0, 'M8')] = sw


    cliente = Cliente()

    cliente.register(maquina)

    pacotes = 0

    if len(argv) > 1:
        pacotes = int(argv[1])

    cliente.iniciar(pacotes, delay=DELAY)


if __name__ == '__main__':
    main()
