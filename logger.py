import re
import os
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class Logger():
	def __init__(self, name, log_location, log_file):
		self.log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
		# self.create_log_folder(log_location)
		self.logFile = os.path.join(log_location, log_file)
  
		self.my_handler = TimedRotatingFileHandler(self.logFile, 
            								  when='midnight', 
                      						  interval=1, 
		                                 	  backupCount=5)
		self.my_handler.setFormatter(self.log_formatter)
		self.my_handler.setLevel(logging.INFO)
		# log
		self.log = logging.getLogger(name)
		self.log.setLevel(logging.INFO)
		self.log.addHandler(self.my_handler)

	def debug(self, message):
		self.log.error(message)	

	def info(self, message):
		self.log.info(message)

	def warning(self, message):
		self.log.warning(message)

	def error(self, message):
		self.log.error(message)

	def critical(self, message):
		self.log.critical(message)

	def create_log_folder(self, directory):
		if not os.path.exists(directory):
			os.mkdir(directory)
