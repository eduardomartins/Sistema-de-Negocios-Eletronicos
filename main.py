# coding: UTF-8
"""

"""
import time
import sys
from maquina import Maquina
from cliente import Cliente
from no import trafego, TAMANHOS
from infra import Lan, ServidorBancoDados, ServidorWeb, ServidorAplicacao, Roteador, Firewall


DELAY = 0.0005
VISITAS = 250


def main(argv=sys.argv):
   
    lan1 = Lan()
    lan2 = Lan()
    fw = Firewall()
    rot = Roteador()
    sw = ServidorWeb()
    sa = ServidorAplicacao()
    bd = ServidorBancoDados()
    
    maquina = Maquina(roteador)
    no = maquina.inicial.add_proximo(Trafego(lan1)).add_proximo(Trafego(sw)).add_proximo(Trafego(sa, 0.95, TAMANHOS.get('M3')))
    
    # Interação 2
    #interacao2 = 
    no.add_proximo(Trafego(sw, 0.2, TAMANHOS.get('M3')))
    
    # Interação 3
    #interacao3 =
     no.add_proximo(Trafego(bd, 0.8, TAMANHOS.get('M6'))).add_proximo(Trafego(sa, 1, TAMANHOS.get('M7'))).add_proximo(Trafego(sw, 1, TAMANHOS.get('M9')))
    
                     
    cliente = Cliente()
    cliente.register(maquina)

    pacotes = 0
    if len(argv) > 1:
        pacotes = int(argv[1])

    cliente.iniciar(pacotes, delay=DELAY)

    return 0



if __name__ == '__main__':
    main()
