__author__ = 'jadams'

import nltk
import os
import re
import unicodedata
import codecs
import collections
import csv
import simplejson as json
import paramiko

class auto(object):
	
	

        def __init__(self):
                print('Welcome. Lets Automate! \nWe will now start tasks...')
	
#CSV Creation
        def creation(self):
                print('opening tyler.csv...')
                self.csv = open('tyler.csv', 'rb')
                self.csvRead = csv.reader(self.csv, delimiter=',')
                auto.tylersList = list(self.csvRead)
                print(self.tylersList)
		auto.tylersList = auto.tylersList.split()
                print(type(at.tylersList))
           
	def connection(self):
                self.X = ('')
		self.ip = at.tylersList[0]
		print(self.ip)
		self.user = at.tylersList[1]
                self.password = at.tylersList[2]
		self.info = []
                print('Opening SSH Connection to tyler.csv Definitions...')
                self.ssh = paramiko.SSHClient()
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(ip, username=self.user, password=self.password)
                stdin , stdout , stderr = ssh.exec_command()
                for line in stdout:
                        self.X = (line.strip())
                        self.info.append(self.X)
                        print(self.X)
                        print('Completed!')
                        print('Closing Connection')
                        self.ssh.close()
                        print('Enjoy your day')

auto.tylersList = []
at = auto()
at.creation()
at.connection()
