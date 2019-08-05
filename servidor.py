# -*- coding: utf-8 -*-
import socket
import os
import sys
import commands

if len(sys.argv) == 1:
    print "É necessario informar a porta para o Servidor escutar"
    sys.exit()
elif sys.argv[1].isdigit() is False:
    print "A Porta do Servidor deve ser definida por um inteiro"
    sys.exit()

HOST = ''              # Endereco IP do Servidor
PORT = int(sys.argv[1])            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)


print "Servidor FTP em Execução. (ctrl + c para parar)"
while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    if pid == 0:
        tcp.close()
        print 'Conectado por', cliente
        msg = con.recv(1024)
        op = msg.split(":")
        if op[0] == 'list':
            var = commands.getoutput("ls data")
            con.send(var)
        elif op[0] == "get":
            arq = open("data/" + op[1], "r")
            for linha in arq:
                con.send(linha)
        elif op[0] == "put":
            arq = open("data/" + op[1], "w")
            # sem esse trecho parte do arquivo entra no primero buffer
            con.send("GO")
            while True:
                dados = con.recv(1024)
                if not dados:
                    print ("Arquivo recebido " + op[1])
                    break
                arq.write(dados)
            arq.close()
        elif op[0] == "rm":
            os.system("rm data/" + op[1])
            print ("Arquivo " + op[1] + " removido por")
        print 'Finalizando conexao do cliente', cliente
        con.close()
        sys.exit(0)
    else:
        con.close()
