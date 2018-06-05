# -*- coding: utf-8 -*-
__autor__ = "Juan Manuel Ruiz Plascencia"
__version__ = "1.0.1"
__email__ ="maniz39@hotmail.com"
__status__ = "Alpha"
"""
This script runs the plataformaSOM application using a development server.
"""

from os import environ
from plataformaSOM import app
from models import Servicios
import bases


if __name__ == '__main__':
    #app.run(debug=True)
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    app.run(debug = True,host = "0.0.0.0", port = 5000)
