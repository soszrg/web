#encoding=utf-8

from bs4 import BeautifulSoup, Comment
import requests
import os

UrlBase = 'http://www.qiushibaike.com'
UrlHot = UrlBase + '/hot/'
EndUrl = UrlBase+'###'

NewAllComments = []
OldAllComments = []
class QiuBai:
    __session = ""
    
    def __init__(self):
        self.__session = requests.session()
        
    def GetBaseHtml(self, url):
        html = self.__session.get(url) 
        baseSoup = BeautifulSoup(html.text, 'html5lib')
        
        allStatus = baseSoup('div', {'class':"article block untagged mb15"}) 
        for one in allStatus:
            self.ParserDiv(one)
        
        nextPageUrl = UrlBase + baseSoup('a', {'class':'next'})[0]['href']
        print nextPageUrl
        if nextPageUrl == EndUrl:
            print '****hot is end***'
            return
        self.GetBaseHtml(nextPageUrl)
    
    def ParserDiv(self, divBase):
        # check whether votes num is more than 500
        votes = divBase('span', {'class':'stats-vote'})[0]('i', {'class':'number'})[0].get_text()
        if int(votes) < 500:
            print 'votes is less than 500'
            return
        # check whether there is image or video
        image = divBase('div', {'class':'thumb'})
        video = divBase('div', {'class':'video_holder'})
        if len(image) or len(video):
            print 'there is a imgae or video'
            return
        
        contentDiv = divBase('div', {'class':'content'})[0]
        # get comment
        comment = contentDiv.find(text=lambda text:isinstance(text, Comment))
        if comment in OldAllComments:
            print 'this status has existed'
            return
        NewAllComments.append(comment)
        # delete comment from content div
        comment.extract() 
        content = divBase('div', {'class':'content'})[0].get_text()#.split()

        # write content into tmp file
        with open('tmp.txt', 'a') as fd:
            fd.write(content.encode('utf-8'));
            fd.write("========\n")
            fd.close
        
if __name__ == "__main__":
    
    if os.path.exists('idRecord.txt'):
        with open('idRecord.txt', 'r') as idReadFd:
            lines = idReadFd.readlines()
            for one in lines:
                tmp = one[0:-1]
                OldAllComments.append(tmp)
            idReadFd.close()
    print OldAllComments
    qiuBai = QiuBai()
    qiuBai.GetBaseHtml(UrlHot)
    
    if os.path.exists('tmp.txt') == False:
        os._exit(0)
        
    with open('tmp.txt', 'r') as inFd:
        with open('content.txt', 'a') as outFd:
            lines = inFd.readlines()
            for line in lines:
                if line.split():# delete space line
                    outFd.write(line)
            outFd.write("All Items:%d" %(len(OldAllComments)+len(NewAllComments)))
            outFd.write("========\n")
            outFd.close()
        inFd.close()
    
    with open('idRecord.txt', 'a') as idWriteFd:
        for one in NewAllComments:
            idWriteFd.write(one+'\n')
        idWriteFd.close()
    os.remove('tmp.txt')
