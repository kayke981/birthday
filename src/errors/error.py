class SenderError(Exception):
	def __init__(self, message):
		super().__init__(message)

class InvalidDate(Exception):
	def __init__(self, message):
		super().__init__(message)