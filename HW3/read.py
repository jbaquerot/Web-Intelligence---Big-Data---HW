### WH3
# server

import glob
import stopwords
import logging
logging.basicConfig(filename='out.log',level=logging.DEBUG)


textFiles = glob.glob('hw3data/*')

def fileContents(fileName):
    f = open(fileName)
    try:
        return f.read()
    finally:
        f.close()
	logging.info('%s closed', f.name)

source = dict((fileName, fileContents(fileName))
              for fileName in textFiles)

f = open('outfile','w')
def final(key,value):
    print key,value
    f.write(srt((key,value)))

# client

def mapfn(key,value):
   for line in value.splitlines():
       for word in line.split():
            yield word.lower(), 1

def reducefn(key, value):
    return key, len(value)

