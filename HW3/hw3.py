#!/usr/bin/env python
### WH3
# server
import mincemeat
import glob
import stopwords


textFiles = glob.glob('hw3data/*')

def fileContents(fileName):
    f = open(fileName)
    try:
        return f.read()
    finally:
        f.close()
    logger.info('%s closed', f.name)

source = dict((fileName, fileContents(fileName))
              for fileName in textFiles)

f = open('outfile','w')

#print '*************', stopwords.allStopWords.keys()
# client

def mapfn(key,value):
   #print 'mapfn - Starting'
   #logger.info('mapfn - Starting')
   for line in value.splitlines():
       #print 'line: ', line
       #logger.info('mapfn - line: %s', line)
       bioInfo=line.split(':::')
       paperId=bioInfo[0]
       authors=bioInfo[1].split('::')
       title=bioInfo[2]
       titleWords=title.split()
       for stopWord in stopwords.allStopWords.keys():
           while stopWord in titleWords:
               titleWords.remove(stopWord)
           while stopWord.upper() in titleWords:
               titleWords.remove(stopWord.upper())
       #print 'paper: ', paperId, ' authors: ', authors, ' title: ', titleWords
       for author in authors:
           for word in titleWords:
                yield author.upper(), word.upper()

def reducefn(key, value):
    #print 'key: ', key, ' value: ', value
    result={}
    for v in value:
        try:
            result[v]+=1
        except KeyError:
            result[v]=1
    return result

s = mincemeat.Server()

s.datasource=source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password='hw3')
for key in results.keys():
    words=results[key]
    for word in words.keys():
        print key, ',', word,',',words[word]
