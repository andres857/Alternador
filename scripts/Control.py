#!/usr/bin/python3
import time
import RPi.GPIO as GPIO


#Configuracion inicial de los puertos
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

#Definicion de Puertos
statusWC =0
lecturaestadoWC=31
cambiarCanal = 15

GPIO.setup(cambiarCanal, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(lecturaestadoWC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Programa
def alternateChannel():
    GPIO.output(cambiarCanal, GPIO.HIGH)
    print ("alto")
    time.sleep(0.5)
    GPIO.output(cambiarCanal, GPIO.LOW)
    print ("bajo")


def statusPorts():
    #Lectura del switch HDMI
    if (GPIO.input(lecturaestadoWC) == GPIO.HIGH):
        statusWC = 1
        print("Canal windows channel")
    else:
        statusWC = 0
        print("Canal Comercial")
    return statusWC
