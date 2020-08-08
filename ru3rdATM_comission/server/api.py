from ru3rdATM_comission.server import server
from ru3rdATM_comission.tools import api_response
from ru3rdATM_comission.server import DB
from flask import request, send_file
import os
from time import time


@server.route("/api/health")
def api_health():
	return api_response(name="HEALTH", code=200, data={"health": "ok"}, description="Health status")


@server.route("/api/get_csv")
def api_get_csv():
	filename = f".tmpcsv{time()}"
	with open(filename, "w+") as csv:
		csv.write(DB.csv)
	r = send_file(filename, as_attachment=True, attachment_filename="3rd-party-ATM-commission.csv")
	os.remove(filename)
	return r


@server.route("/api/get_info/<int:index>")
def api_get_info(index):
	info = DB.bank_info(index).to_dict()
	return api_response(name="BANK_INFO", data={"bank_name": info["Банк"][index], "Возможность": info["Возможность"][index]})
