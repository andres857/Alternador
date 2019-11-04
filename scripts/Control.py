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
    print ("alto.control")
    time.sleep(0.5)
    GPIO.output(cambiarCanal, GPIO.LOW)
    time.sleep(1.5)
    print ("bajo.control")


def statusPorts():
    #Lectura del switch HDMI
    if (GPIO.input(lecturaestadoWC) == GPIO.HIGH):
        statusWC = 1
        full_filename = "../static/images/logoWC.png"
        templateData = {
           'Signal': 'Canal Institucional'
           }
        print("Canal windows channel")
    else:
        statusWC = 0
        full_filename = "../static/images/une.png"
        templateData = {
           'Signal': 'Canal Comercial',
           }
        print("Canal Comercial")

    return statusWC,full_filename,templateData
