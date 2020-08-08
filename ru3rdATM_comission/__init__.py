def start_api_server():
	from ru3rdATM_comission.server import server

	server.run(host="0.0.0.0", port=9854)

start_api_server()