_author__ = 'JohnAdams'

import itertools
import os
import re
import unicodedata
import codecs
import collections
import csv
import shutil
import cgi

import os



class KnowledgeBaseArticles(object):
    def __init__(self):
        self.kbaKeys = []
        self.matched = []
        self.sigLineList = []
        self.siglinesFound = []
        self.summaries= []
        self.kbaFound = []
        self.book = {'kb0': 'Stopping', 'kb1': 'capture.sh: Captured on'}
        self.check = ''
        self.KnowledgeBasic = {'kb0': 'KBA has found process Death',
                                      'kb1': 'We have found a capture!'}

    def prepKBA(self):
        library = kba.book
        for item in library.keys():
            self.check = library.values()
        print('List Created:')
        print(self.check)


    def searchKBA(self):
        library = kba.book
        for kba.siglinesFound in kba.book.values():
            kba.kbaFound = kba.siglinesFound
        print('debug check:')
        print(kba.kbaFound)
        for line in library.values():
            if line in kba.siglinesFound:
                kba.matched.append(line)
        print('debug Check')
        print(kba.matched)
        for string in kba.matched:
            if string in kba.KnowledgeBasic.values():
                kba.summaries = kba.KnowledgeBasic.keys()[kba.KnowledgeBasic.values().index(string)]
        print('Checking Summaries Found')
        print(kba.summaries)


class crunchText(object):
    kba = KnowledgeBaseArticles()
    fileDef = 'none'

    def __init__(self):
        print('\n')
        print('Welcome to KnowledgeBasic! \n')
        self.currentCount = 1

    def analyzer(self):
        def search(linelist, logfile):
            for line in linelist:
                for log in logfile:
                    if line in log:
                        kba.siglinesFound.append(line)
            return None
        kba.prepKBA()
        print('Check File against KnowlegeBasic')
        print('Please Input Filename')
        self.file = raw_input()
        self.log = open(self.file, 'r')
        self.logRaw = self.log.read()
        self.logs = self.logRaw.splitlines()
        search(kba.check, self.logs)
        print('\n')
        print('Significant Lines Found...' + '\n')
        print(kba.siglinesFound)
        kba.searchKBA()
        print('The Matched KBA summaries''\n')
        print(kba.summaries)
        print('\n')
        print('Removing History''\n')
        kba.summaries = []
        print('History has been cleared''\n')


    def define(self):
        print('Define New Knowledge Basic Article')
        print('Please define article summary')
        self.countString = str(self.currentCount)
        createKBA = 'KB' + self.countString
        self.createKBA = createKBA
        self.summary = raw_input()
        self.BasicAppend = kba.KnowledgeBasic
        self.BasicAppend.update({ct.createKBA: ct.summary})
        self.results = kba.KnowledgeBasic
        print('Done')
        print("Define KBA Significant Lines: Separate lines by ',' :")
        self.siglines = [raw_input()]
        self.linesAppend = kba.book
        self.linesAppend.update({ct.createKBA: ct.siglines})
        print('Done')
        print('New Definition Completed')
        self.currentCount = self.currentCount + 1
        print('Next KBA Entry' + str(self.currentCount))

    def prompt(self):
        print('\n')
        print('Menu:  u = upload(RemovedForNow!!!)  a = Analyze d = Define  p = Print KBAs/SigLineRef')
        self.option = raw_input()
        while self.option != 'q':
            if self.option == 'a':
                self.analyzer()
                print('\n''Completed... Heading Back to Menu''\n')
                break
            elif self.option == 'd':
                self.define()
                print('\n''Completed... Heading Back to Menu''\n')
                break
            elif self.option == 'p':
                print('\n Current Knowledge Basic Library Items:')
                print(kba.KnowledgeBasic)
                print('\n Current KBA Significant Lines:')
                print(kba.book)
                print('\n''Completed... Heading Back to Menu''\n')
                print('\n Checking Summaries is empty')
                print(kba.summaries)
                print('Checking "check" values')
                print(kba.check)
                break


ct = crunchText()
kba = KnowledgeBaseArticles()

a = 1
while a == a:
    ct.prompt()



# for item in self.countKB:
#        resultsString = open('results.txt', 'w')
#        resultsString.write(self.prep)
#        resultsFile = open('results.csv', 'w')
#        wr = csv.writer(resultsFile, delimiter=' ', lineterminator='\n')
#        wr.writerows(self.results)


# def searchBoook(library):
#    for key in library:
#       print library[key]
