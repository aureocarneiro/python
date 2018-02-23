#!/usr/bin/python
# -*- coding: utf-8 -*-

# Módulo necessário

import serial

# Inicialização da interface serial

serial_interface1 = serial.Serial(port = "/dev/ttyUSB0",
                                 baudrate = 4800,
                                 bytesize = serial.SEVENBITS,
                                 parity = serial.PARITY_EVEN,
                                 stopbits = serial.STOPBITS_ONE)

serial_interface2 = serial.Serial(port = "/dev/ttyUSB1",
                                 baudrate = 4800,
                                 bytesize = serial.SEVENBITS,
                                 parity = serial.PARITY_EVEN,
                                 stopbits = serial.STOPBITS_ONE)

# Trecho de código necessário para desconsiderarmos a primeira leitura que chega da sonda, que
# eventualmente será capturada "pela metade".

data1 = serial_interface1.read(1)
data2 = serial_interface2.read(1)

while (data1 != "\n"):
    data1 = serial_interface1(1)

while (data2 != "\n"):
    data2 = serial_interface2(1)

# Laço

while (True):

    # Lê os oito caracteres enviados pela sonda
    data1 = serial_interface1.read(8)
    data2 = serial_interface2.read(8)

    # Calcula o valor da taxa de dose instantânea (em uSv/h)
    dose_rate1 = float(data1[3:6]) * (10 ** (int(data1[2]))) * 0.001
    dose_rate2 = float(data2[3:6]) * (10 ** (int(data1[2]))) * 0.001
    dose_rate3 = dose_rate1 + dose_rate2

    # Imprime na tela o resultado
    print("Gamma: " + "{0:.3f}".format(dose_rate1) + " uSv/h")
    print("Neutron: " + "{0:.3f}".format(dose_rate2) + " uSv/h")
    print("Total: " + "{0:.3f}".format(dose_rate2) + " uSv/h")
