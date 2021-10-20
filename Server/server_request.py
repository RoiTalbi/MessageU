

"""
A simple Stracture to hold request data
"""
class Request():
	
	def __init__(self, client_id, version, code, payload_size, payload):
		self.client_id = client_id
		self.version = version
		self.code = code
		self.payload_size = payload_size
		self.payload = payload


	def __str__(self):
		formatted_str = f"Cliend ID = {self.client_id} \n Version = {self.version}\n Code = {self.code}\n Payload size = {self.payload_size}\n Payload = {self.payload}\n"
		return formatted_str


