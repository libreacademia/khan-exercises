# i18n implementation for Khan Academy exercise framework
# following the RFC3066 whe use (x)-(y) where x is a ISO698 language code
# and y is a ISO3166 conuntry code, for example es-ES es-AR es-UY

import os
import sys
from HTMLParser import HTMLParser
# from htmlentitydefs import name2codepoint


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    #def handle_starttag(self, tag, attrs):
       # print "Encountered a start tag:", tag

    #def handle_endtag(self, tag):
        # print "Encountered an end tag :", tag

    def handle_data(self, data):
        if (data != ''):
            print "Encountered some data  :", data


def createDirIfNotExists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return os.path.exists(dir)


def getCultureArgument():
    return sys.argv[1]


path = "../exercises"  # insert the path to the directory of interest
dictPath = '../dictionaries'
dirList = os.listdir(path)
culture = getCultureArgument()
outputPath = dictPath + '/' + culture

createDirIfNotExists(dictPath)
createDirIfNotExists(outputPath)

for arg in sys.argv:
    print arg

for fname in dirList:
    fileName = os.path.splitext(outputPath + '/' + fname)[0] + '.json'
    file = open(fileName, 'w+')


file = open('../exercises/absolute_value.html', 'r')
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(file.read())
