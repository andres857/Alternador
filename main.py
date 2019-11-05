#!/usr/bin/python3
import os
from flask import Flask, render_template, request
from scripts import Control

app = Flask(__name__)
#app.config['SERVER_NAME']='alternador:80'

@app.route("/")
def index():
    statusWC,full_filename,templateData = Control.statusPorts()
    return render_template('index.html',imagenesupo=full_filename, **templateData)

@app.route("/Une")
def pagUne():
    statusWC,full_filename,templateData = Control.statusPorts()
    if statusWC==0:
        pass
    else:
        Control.alternateChannel()
        statusWC,full_filename,templateData = Control.statusPorts()
    return render_template('Une.html',imagenesupo=full_filename, **templateData)

@app.route("/Imbanaco")
def pagImbanaco():
    statusWC,full_filename,templateData = Control.statusPorts()
    if statusWC==1:
        pass
    else:
        Control.alternateChannel()
        statusWC,full_filename,templateData = Control.statusPorts()
    return render_template('ImbanacoTV.html ',imagenesupo=full_filename, **templateData)

@app.route("/Dispositivos")
def receptores():
    return render_template('Dispositivos.html')











if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
