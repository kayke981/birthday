from typing import (Optional)
from datetime import datetime

class Birthday:
	def __init__(self, send_sms: Optional[bool] = True, send_email: Optional[bool] = False, message: Optional[str] = 'Happy Birthday! <3', *, year: int, day: int, month: int, your_name: str):
		self.send_sms = send_sms
		self.send_email = send_email
		self.message = message
		self.year = year
		self.day = day
		self.month = month
		self.your_name = your_name
	
	def calc(self):
		d1 = datetime(self.year,self.month,self.day,self.hour)
		d2 = datetime.now()
		
		diff = d1 - d2
		
		days = diff.days
		years, days = days // 365, days % 365
		months, days = days // 30, days % 30
		seconds = diff.seconds
		hours, seconds = seconds // 3600, seconds % 3600
		minutes, seconds = seconds // 60, seconds % 60
		self.years = years
		self.months = months
		self.days = days
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
	