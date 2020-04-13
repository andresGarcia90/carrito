#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import os
sys.path.insert(0,'lib/')
from clase_principal import ppal


#Metodo principal
def main():   
    version = 1.0
    id_cliente = 0;
    id_local = 0;

    # Manejo de parametros de la llamda principal
    if len(sys.argv) > 1:
        # print('lista de argumentos', sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--verbose", help="Mostrar información de depuración.", action="store_true")
        parser.add_argument("-c", "--cliente", help="Id del cliente.")
        parser.add_argument("-l", "--local", help="Id local.")
        args = parser.parse_args()     

        if args.verbose:
            print('Version:',version)
            exit(1)
        if args.cliente:
            id_cliente = int(args.cliente)
        if args.local:
            id_local = int(args.local)
        if id_cliente <= 0:
            print('id cliente invalido')
            exit(1)
        else:
            if id_local <= 0:
                print(' id local invalido')
                exit(1)
            else:
                print('Llamo al metodo principal')
                #LLamamos a la clase principal
                ppal(id_cliente,id_local)
    else:
        print('Error: faltan parametros')
        exit(1)

main()