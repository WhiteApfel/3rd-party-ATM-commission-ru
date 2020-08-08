def api_response(name: str, data: dict = None,code: int = 200, description: str = None):
	r = {"code": code, "name": name}
	if description:
		r["description"] = description
	if data:
		r["data"] = data
	return r
