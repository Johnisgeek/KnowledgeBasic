__author__ = 'jadams'

import numpy as np
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
        self.tylersList = []
        print('Welcome. Lets Automate! \nWe will now start tasks...')

    # CSV Creation
    def creation(self):
        print('opening tyler.csv...')
        self.csv = open('tyler.csv', 'rb')
        self.csvRead = csv.reader(self.csv)
        self.tylersListPrep = list(self.csvRead)
        print(self.tylersListPrep)
        self.tylersList = np.asarray(self.tylersListPrep)
        print(type(self.tylersList))
        print(self.tylersList)

    def connection(self):
        self.X = ('')
        self.ip = at.tylersList[0,0]
        print(self.ip)
        self.user = at.tylersList[0,1]
        self.password = at.tylersList[0,2]
        self.info = []
        self.command = at.tylersList[0,3]
        print('Opening SSH Connection to tyler.csv Definitions...')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, username=self.user, password=self.password)
        stdin, stdout, stderr = self.ssh.exec_command(self.command)
        for line in stdout:
            self.X = (line.strip())
            self.info.append(self.X)
            print(self.X)
            self.ssh.close()
        print('Completed!')
        print('Closing Connection')
        print('Enjoy your day')


at = auto()
at.creation()
at.connection()

///
pi@raspberrypi:~ $ sudo python tyler.py
Welcome. Lets Automate!
We will now start tasks...
opening tyler.csv...
[['192.168.2.108', 'pi', 'raspberry', 'ls', 'tyler.csv']]
<type 'numpy.ndarray'>
[['192.168.2.108' 'pi' 'raspberry' 'ls' 'tyler.csv']]
192.168.2.108
Opening SSH Connection to tyler.csv Definitions...
bootlog
bootlog.save
camera
check.txt
Desktop
Documents
Downloads
edit.py
ftp
get-pip.py
LCD-show
main.py
matchbox-keyboard
Music
nltk_data
paramikoNeeds
phantom.log
phantomLog.save
phantomLog.save.1
Photos
Pictures
Public
python_games
results.csv
resultsJson.txt
results.txt
song.mp4
Templates
tyler.csv
tyler.py
tyler.py.save
tyler.py.save.1
Videos
xinput-calibrator.deb
Completed!
Closing Connection
Enjoy your day
///
