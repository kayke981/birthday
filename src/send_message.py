import os
from twilio.rest import Client
from src.errors import SenderError
from src.functions.sender import sms, email
from smtplib import SMTP_SSL
from ssl import create_default_context

class Sender:
	def __init__(self, sid: str, auth: str, body: str, to: str):
		self.sid = sid
		self.auth = auth
		self.body = body
		self.to = to
		self._sE = email
		self._cS = sms
		
	def set_keys(self):
		os.environ["SID"] = self.sid
		os.environ["AUTH"] = self.auth
		
		auth = os.environ["SID"]
		sid = os.environ["AUTH"]
		
	def send_sms(self, _from: str):
		sid = self.sid
		auth = self.auth
		
		client = Client(sid, auth)
		
		try:
			self._cS(client).send_sms(body=self.body, _from=_from, to=self.to)
			return True
		
		except (Exception) as err:
			if 'was not found' in err:
				raise SenderError('sid {} and auth {} are invalid'.format(sid, auth))
			raise SenderError(f'Something is wrong. Error recived:\n {err}')
	
	def send_email(self, email, password):
		context = create_default_context()
		
		server = SMTP_SSL("smtp.gmail.com", port=465,  context=context)
		self._sE(server).login(email, password)
		self._sE(server).send_mail(self.to, self.body)