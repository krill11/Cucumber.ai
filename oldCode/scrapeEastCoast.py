import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd

def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()

def makeTable (link):
    xhtml = url_get_contents(link).decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    count = 11
    finalTable = []
    while list(p.tables[0])[count][0] != 'MEAN':
        if list(p.tables[0])[count][0] == 'MEAN':
            print('done')
        count += 1
    finalTable = list(p.tables[0])[count]
    
    for x in range(finalTable.count('')):
        finalTable.remove('')
    finalTable.remove('MEAN')
    for x in range(len(finalTable)):
        finalTable[x] = float(finalTable[x])
    return finalTable

def findAvg(arr):
    return sum(arr)/len(arr)

def monthlyAverage(cityStr, stateStr, monthInt):
    finalLink = 'https://wrcc.dri.edu/cgi-bin/cliMONtavt.pl?'
    finalLink += str(stateStr.lower())
    finalLink += "".join(cityStr.split()).lower()[0 : 4]
    monthInt = int(monthInt)
    return(makeTable(finalLink)[monthInt - 1])

def average(cityStr, stateStr):
    finalLink = 'https://wrcc.dri.edu/cgi-bin/cliMONtavt.pl?'
    finalLink += str(stateStr.lower())
    finalLink += "".join(cityStr.split()).lower()[0 : 4]
    return(findAvg(makeTable(finalLink)))