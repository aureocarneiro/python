#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. Ler os tamanhos das janelas de tempo para o cáculo da média móvel que resulta na taxa de dose
#    instantânea mostrada na IHM. Ler tanto para a sonda de gamma quanto para a de nêutrons.
#    Interpretar o resultado levando em conta as explicações do manual relacionadas.
# 2. Modificar o programa de comunicação serial para que ele sempre exiba em um terminal os mesmos valores mostrados
#    na IHM (taxa de dose instantânea e taxa de dose média) para as duas sondas.

# Módulo necessário

import socket

# Função que inclui o checksum e o caractere <ETX> a qualquer mensagem que se deseja enviar

def format_message(message):
    checksum = ord(message[3]) ^ ord(message[4])
    for character in message[5:]:
        checksum ^= ord(character)
    return (message + "{0:02X}".format(checksum) + "\x03")


# Cria socket TCP/IP para comunicação com o SATURN I 5700 RTM da sonda de gamma

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.100", 1001))

# Requisita os valores das janelas de tempo para cáculo da média móvel
# COLOCAR TB O VALOR O THRESHOLD LEVEL 01001GL RESPOSTA: (STX)01024GL1234.56:1234.56:1234.56
#(CS)(CS) (ETX)
client_socket.send(format_message("\x0201001GN"))
data = client_socket.recv(1024)

# Imprime os valores lidos na tela

print("Sample number of the 1st window: " + data[8:11])
print("Sample number of the 2nd window: " + data[11:14])
print("Sample number of the 3th window: " + data[14:17])
print("Sample number of the 4th window: " + data[17:20])
print("Falling threshold %: " + data[20:23])

# Fecha a conexão

client_socket.close()
