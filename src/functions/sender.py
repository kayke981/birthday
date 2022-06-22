from typing import (Any)

class sms:
	def __init__(self, Client: Any) -> None:
		self.client = Client
	
	def send_sms(self, _from: str, to: str, body: str):
		self.client.messages.create(from_=_from, to=to, body=body)

class email:
	def __init__(self, Server: Any) -> None:
		self.server = Server
	
	def login(self, email: str, password: str):
		self.email = email
		self.server.login(email, password)
	
	def send_mail(self, to: str, body: str):
		self.server.sendmail(self.email, to, body)