import os,json

class dumb(object):
	def __init__(self):
		vcap_services=json.loads(os.getenv("VCAP_SERVICES"))
		sqlservices=vcap_services[u"mysql"][0]
		self.name=sqlservices[u"credentials"][u"name"]
		self.hostname=sqlservices[u"credentials"][u"hostname"]
		self.port=sqlservices[u"credentials"][u"port"]
		self.username=sqlservices[u"credentials"][u"username"]
		self.password=sqlservices[u"credentials"][u"password"]
		self.uri=sqlservices[u"credentials"][u"uri"]
		self.jdbcUrl=sqlservices[u"credentials"][u"jdbcUrl"]
		
sql=dumb()