# Ftp basico em python
Servidor de arquivos básico em Python

O programa é um servidor de arquivos em python com dois arquivos:
 - cliente.py
 - servidor.py
 
Execução:

Servidor

-python servidor.py <porta_a_escutar>

Cliente

LISTAR:

-python cliente.py <ip_servidor> <porta_servidor> list

BAIXAR:

-python cliente.py <ip_servidor> <porta_servidor> <nome do arquivo no servido> <nome do arquivo a ser salvo localmente>

UPAR:

-python cliente.py <ip_servidor> <porta_servidor> <nome do arquivo local> <nome do arquivo no a ser salvo no servidor>

REMOVER DO SERVIDOR:

-python cliente.py <ip_servidor> <porta_servidor> <nome do arquivo>

OBS: junto do arquivo servidor.py deve haver um diretório chamado data. Onde ficaram os arquivo salvos no mesmo. 
