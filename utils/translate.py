# i18n implementation for Khan Academy exercise framework
# following the RFC3066 whe use (x)-(y) where x is a ISO698 language code
# and y is a ISO3166 conuntry code, for example es-ES es-AR es-UY

import os
import sys
import linecache
from HTMLParser import HTMLParser
# from htmlentitydefs import name2codepoint


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    fileName = ''
    output = []
    parsingTitleTag = False

    def get_output(self):
        jsonString = "{\n"
        for value in self.output:
            jsonString += '    "' + value + '" : "' + value + '",\n'
        jsonString += "}\n"
        return jsonString

    def set_fileName(self, fname):
        self.fileName = fname

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'p':
            self.extract_words( linecache.getline(self.fileName, self.getpos()[0]) )
        elif tag.lower() == 'title':
            self.parsingTitleTag = True

    def handle_endtag(self, tag):
        self.parsingTitleTag = False

    def handle_data(self, data):
        if self.parsingTitleTag:
            print data + "####"
            self.output.append(data)

    def extract_words(self, s):
        s = s[s.find('>') + 1:]
        while s.find('<code') >= 0 :
            sentence = s[:s.find('<code')]
            self.output.append( sentence )
            s = s[s.find('</code>') + len('</code>'):]
        sentence = s[:s.find('</p>')]
        self.output.append(sentence)
        empty = True



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

for fname in dirList:
    fileName = os.path.splitext(outputPath + '/' + fname)[0] + '.json'
    file = open('../exercises/' + fname, 'r')
    print "---- " + file.name + "----"
    parser = MyHTMLParser()
    parser.set_fileName(file.name)
    parser.feed(file.read())
    print parser.get_output()
    break
