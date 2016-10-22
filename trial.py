_author__ = 'JohnAdams'

import nltk
import os
import re
import unicodedata
import codecs
import collections
import csv
from nltk.compat import raw_input
import shutil
import cgi



class KnowledgeBaseArticles(object):
    def __init__(self):
        self.sigLineList = []
        self.significantLines = {'kb0': ['xlicense: ERROR! ERR_STATE_ERR(-18)Confd not running']}
        self.KnowledgeBasic = {'kb0':'This Knowledge Base Article verifies if ConfD process has died.  Technician'
                               'will need to access root and fsck all partitions', 'processWatch':'Process Watch has'
                               'found dead processes.'}

class crunchText(object):
    fileDef = 'none'



    def __init__(self):
        self.accountDir = '/'
        self.uploadDir = self.accountDir
        print('Welcome to KnowledgeBasic! \nPlease Press Enter to Proceed...')
        self.currentCount = 1



    def processWatch(self):
        print('Check File for Process Death')
        print('Please Input Filename')
        file = raw_input('')
        self.log = open(file, 'r')
        self.logRaw = self.log.read()
        self.logs = self.logRaw.splitlines()
        self.processWatch = ['Stopping xhad...', 'Stopping xactiond', 'Stopping xconfigd...']
        self.countProcessWatch = set(self.processWatch) & set(self.logs)
        self.percentProcessWatch = float(len(self.countProcessWatch)) / float(len(self.processWatch))
        self.percentInt = int(self.percentProcessWatch * 100)
        self.prep = repr(self.countProcessWatch)
        self.results = [self.prep]
        print('the messages found in common:')
        print(self.countProcessWatch)
        print('the likely match to KnowledgeBasic0 is:')
        print(self.percentInt)
        print('Creating Result Files...')
        for item in self.countProcessWatch:
            resultsString = open('results.txt', 'w')
            resultsString.write(self.prep)
            resultsFile = open('results.csv', 'w')
            wr = csv.writer(resultsFile, delimiter=' ', lineterminator='\n')
            wr.writerows(self.results)


    def checkKB(self):
        def search(lines, logs):
                for k in lines:
                    for v in lines(k):
                        if logs in v:
                            print(k)
                            return k
                return None
        print('Check File against KnowlegeBasic')
        print('Please Input Filename')
        self.file = raw_input()
        self.log = open(self.file, 'r')
        self.logRaw = self.log.read()
        self.logs = self.logRaw.splitlines()
        lines = str(kba.significantLines)
        logs = ct.logs
        self.newResults = search(lines, logs)
        print(self.newResults)
        self.countKB = set(kba.significantLines) & set(self.log)
        self.prep = repr(self.countKB)
        self.results = [self.prep]
        print('the messages found in common:')
        print(self.countKB)
        print('Creating Result Files...')
        for item in self.countKB:
            resultsString = open('results.txt', 'w')
            resultsString.write(self.prep)
            resultsFile = open('results.csv', 'w')
            wr = csv.writer(resultsFile, delimiter=' ', lineterminator='\n')
            wr.writerows(self.results)





    def upload(self):
        print('Upload Log file to KnowledgeBasic Server')
        print('Please Print File Name')
        self.file = raw_input()
        print('Please Print Directory Path')
        self.uploadDir = raw_input()
        self.uploadFile= self.uploadFile(self.file, self.uploadDir)
        self.form = cgi.FieldStorage()
        if not self.form.has_key(self.file):
            return
        self.fileitem = self.form[self.file]
        if not self.fileitem.file:
            return
        self.outpath = os.path.join(self.uploadDir, self.fileitem.filename)
        with open(self.outpath, 'wb') as fout:
            shutil.copyfileobj(self.fileitem.file, fout, 100000)

    def define(self):
        print('Define New Knowledge Basic Article')
        print('Please define article summary')
        self.countString = str(self.currentCount)
        createKBA = 'KB'+ self.countString
        self.createKBA = createKBA
        self.summary = raw_input()
        self.BasicAppend = kba.KnowledgeBasic
        self.verification = raw_input()
        self.BasicAppend.update({ct.createKBA: ct.summary})
        self.results = kba.KnowledgeBasic
        print('Done')
        print("Define KBA Significant Lines: Separate lines by ',' :")
        self.siglines = []
        self.siglines = raw_input()
        self.linesAppend = kba.significantLines
        self.verification2 = raw_input()
        self.linesAppend.update({ct.createKBA: ct.siglines})
        self.results2 = kba.significantLines
        print('Done')






        print('New Definition Completed')
        self.currentCount= self.currentCount + 1
        print('Next KBA Entry'+ str(self.currentCount))



    def prompt(self):
        print('Menu:  u = Upload  a = Analyze d = Define  p = Print KBAs/SigLineRef')
        self.option = raw_input()
        while self.option != 'q':
            if self.option == 'a':
                self.checkKB()
                print('Completed... Heading Back to Menu')
                break
            elif self.option == 'u':
                self.upload()
                print('Completed... Heading Back to Menu')
                break
            elif self.option == 'd':
                self.define()
                print('Completed... Heading Back to Menu')
                break
            elif self.option == 'p':
                print(kba.KnowledgeBasic)
                print(kba.significantLines)
                break




ct = crunchText()
kba = KnowledgeBaseArticles()

a=1
while a == a :
    ct.prompt()
