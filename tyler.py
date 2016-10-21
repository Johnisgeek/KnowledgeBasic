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
                self.tylersList = list(self.csvRead)
                print(self.tylersList)
                print(type(self.tylersList))
            
            
#SSH CONNECTION
        def connection(self):
                self.X = ('')
		self.ip = at.tylersList[0]
		self.
                self.info = []
                print('Opening SSH Connection to tyler.csv Definitions...')
                self.ssh = paramiko.SSHClient()
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(at.tylersList(0), username=at.tylersList(1), password=at.tylersList(2))
                stdin , stdout , stderr = ssh.exec_command()
                for line in stdout:
                        self.X = (line.strip())
                        self.info.append(self.X)
                        print(self.X)
                        print('Completed!')
                        print('Closing Connection')
                        self.ssh.close()
                        print('Enjoy your day')


at = auto()
at.creation()
at.connection()
