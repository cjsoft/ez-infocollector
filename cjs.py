import os,json

class dumb(object):
	def __init__(self):
		vcap_services=json.loads(os.getenv("VCAP_SERVICES"))
		sqlservices=vcap_services["mysql"][0]
		self.name=sqlservices["credentials"]["name"]
		self.hostname=sqlservices["credentials"]["hostname"]
		self.port=sqlservices["credentials"]["port"]
		self.username=sqlservices["credentials"]["username"]
		self.password=sqlservices["credentials"]["password"]
		self.uri=sqlservices["credentials"]["uri"]
		self.jdbcUrl=sqlservices["credentials"]["jdbcUrl"]
sql=dumb()