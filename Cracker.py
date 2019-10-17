
'''
TODO LIST:
	Fix and make proxy function better
	Sort code again
	Add help function to all "Yes/no" questions
	Add help  function to "Press enter to exit input"
'''
import requests
import json
import time
import os
import random
import sys

#Help function
def Input(text):
	value = ''
	if sys.version_info.major > 2:
		value = input(text)
	else:
		value = raw_input(text)
	return str(value)

#The main class
class Instabrute():
	def __init__(self, username, passwordsFile='pass.txt'):
		self.username = username
		self.CurrentProxy = ''
		self.UsedProxys = proxy.txt
		self.passwordsFile = pass.txt
		
		#Check if passwords file exists
		self.loadPasswords()
		#Check if username exists
		self.IsUserExists()


		UsePorxy = Input('[*] Do you want to use proxy (y/n): ').upper()
		if (UsePorxy == 'N' or UsePorxy == 'No'):
			self.randomProxy()


	#Check if password file exists and check if he contain passwords
	 
