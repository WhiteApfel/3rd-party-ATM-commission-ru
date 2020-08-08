from flask import Flask
from ru3rdATM_comission.tools import DBTools

DB = DBTools()

server = Flask("3rd party ATM commission API")

from ru3rdATM_comission.server import api
