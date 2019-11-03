#!/usr/bin/python3
import os
from flask import Flask, render_template, request
from scripts import Control

app = Flask(__name__)

@app.route("/")
def index():
    statusWC=Control.statusPorts()
    if (statusWC == 0):
       full_filename = "../static/images/une.png"
       templateData = {
          'Signal': 'Canal Comercial',
          'Canal' : 'Caracol Televison'
          }
    else:
       full_filename = "../static/images/logoWC.png"
       templateData = {
          'image-canal':'logoWC.png',
          'Signal': 'Canal Institucional'
          }

    SwitchChannel = request.args.get('switchChannel')
    print (SwitchChannel)
    if (SwitchChannel == '1'):
        Control.alternateChannel()
        print("Alternando canal from web")

    return render_template('index.html',imagenesupo=full_filename, **templateData )

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
