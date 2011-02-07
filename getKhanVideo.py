#!/usr/bin/python

import urllib2, re, sys
'''
This script is for downloading videos from http://www.khanacademy.org
It accepts keyword as command line argument and stores links to the file

TODO
----
* wget keyword is unnecessary since wget -i takes the list
* implement getopt
'''

if len(sys.argv) == 2:
    keyWord = sys.argv[1]
else:
    keyWord = 'cosmology'

print 'keyWord = ' + keyWord

url = 'http://www.khanacademy.org'

    
def getLinks(url):
    page = urllib2.urlopen(url)
    print 'fetching ' + url + '\n'
    spage = page.read()
    page.close()
    print 'done ...\n'
    return re.findall('/video[^"]*' + keyWord + '[^"]*',spage,re.IGNORECASE)


def getVideo(list,url=url):
    videos = []
    for link in list:
        if type(link) != 'NoneType':
            print 'fetching video ' + link + '\n'
            page = urllib2.urlopen(url + link)
            spage = page.read()
            page.close()
            video = re.search('http:.*.flv',spage,re.IGNORECASE)
            if video:
                videos.append(video.group())
    return videos

def saveList(list, keyWord = keyWord):
    print 'saving list as ' + keyWord + '\n' 
    f = open(keyWord.lower() + '.sh','w')
    f.writelines(list)
    f.close()
    print 'done ...\n'
list = getLinks(url)
videos = getVideo(list)
wgetLinks = map(lambda s: 'wget ' + s + '\n', videos)
saveList(wgetLinks)



    
    
