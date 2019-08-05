# -*- coding: utf-8 -*-
import socket
import sys

HOST = sys.argv[1]  # Endereco IP do Servidor
PORT = int(sys.argv[2])  # Porta que o Servidor esta
op = sys.argv[3]


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)


if op == "list":
    tcp.send(op + ":")
    resposta = tcp.recv(1024)
    print "Arquivos: \n"
    print resposta
    print "##################"
elif op == "get":
    arqRemoto = sys.argv[4]
    arqLocal = sys.argv[5]
    tcp.send(op + ":" + arqRemoto)
    arq = open(arqLocal, 'w')
    while True:
        dados = tcp.recv(1024)
        if not dados:
            print "Arquivo recebido"
            break
        arq.write(dados)
    arq.close()
elif op == "put":
    arqLocal = sys.argv[4]
    arqRemoto = sys.argv[5]
    tcp.send(op + ":" + arqRemoto)
    arq = open(arqLocal, 'r')
    wait = tcp.recv(1024)
    if wait == "GO":
        for linha in arq:
            tcp.send(linha)
    print "Arquivo enviado"
    arq.close()
elif op == "rm":
    arq = sys.argv[4]
    tcp.send(op + ":" + arq)
else:
    print "############################################################################"
    print "Informe os parametros corretamente"
    print "LISTAR: python cliente.py <ip_servidor> <porta_servidor> list"
    print "BAIXAR: python cliente.py <ip_servidor> <porta_servidor> <nome do arquivo no servido> <nome do arquivo a ser salvo localmente>"
    print "UPAR: python cliente.py <ip_servidor> <porta_servidor> <nome do arquivo local> <nome do arquivo no a ser salvo no servidor>"
    print "REMOVER DO SERVIDOR: python cliente.py <ip_servidor> <porta_servidor> <nome do arquivo>"
    print "############################################################################"
tcp.close()
