#encoding=utf-8

import sys
import os
import urllib2
from bs4 import BeautifulSoup
from baseClass.SpiderBase import SpiderBase
import socket
from time import sleep

UrlBase = "http://www.meizitu.com/"
MeituiUrl = 'http://www.meizitu.com/a/sifang_5_' 
QingchunUrl = 'http://www.meizitu.com/a/qingchun_3_'
QunluoUrl = 'http://www.meizitu.com/tag/quanluo_4_'
XingganUrl = ''
AllPic = 'http://www.meizitu.com/a/list_1_'

Max_Page_Num = 30
DirName = 'meizitu/'
GetUrl = QingchunUrl

class Image(SpiderBase):
    __AllImageUrls = []
    __BlumCount = 0
    __PageCount = 1
    name = ''
    
    def __init__(self, url=None, session=None, name=''):
        SpiderBase.__init__(self, url, session)
        self.name = name
        self.__getCount = 0
     
    def AllBlumCount(self):
        return len(self.__AllImageUrls)
       
    def run(self):
        
        print '***Thread[%d] start working***' %self.name
        while (True):
            if self.LockBase.acquire():
                if len(self.__AllImageUrls) == 0:
                    self.LockBase.release()
                    print '***thread[%s] exit' %self.name
                    break
                
                oneBlum = self.__AllImageUrls.pop(0)
                self.LockBase.release()

                print '***thread[%s] start to get [%s] blum' %(self.name, oneBlum['url'])
                self.GetImageData(oneBlum)
                
    def GetSifangImageUrl(self, url=None):
#         self.__PageCount = 1
        print '=====start to get page[%d] albums=====%s' %(self.__PageCount, url)
        html = ''
        try:
            if url == None:
                html = self.SessionBase.get(self.UrlBase)
            else:
                html = self.SessionBase.get(url)
        except Exception as e:
            print e
            if self.__getCount > 3:
                self.__getCount = 0
                return 
            self.__getCount += 1
            if url == None:
                self.GetSifangImageUrl(self.UrlBase)
            else:
                self.GetSifangImageUrl(url)
            
        html.encoding = 'gb2312'
        baseSoup = BeautifulSoup(html.text, 'html5lib')
#         print html.text
        blumLis = baseSoup('li', {'class':'wp-item'})
        for blum in blumLis:
            blumUrl = blum('div', {'class':'pic'})[0].a['href']
            
            newBlum = {}
            newBlum['url'] = blumUrl
            items = blumUrl.split('/')
            newBlum['num'] = items[-1]#+'-%s' %blumName
            
            self.__AllImageUrls.append(newBlum)
            self.__BlumCount += 1
#             print blumName.decode('utf8')
        
        pageLis = baseSoup('div', {'id':'wp_page_numbers'})[0].select('li')
        for li in pageLis:
            if li.get_text() == u'下一页':
                self.__PageCount += 1
                if self.__PageCount > Max_Page_Num:
                    print '===page[%d] to max page===' %self.__PageCount
                    self.__PageCount = 1
                    return
                
                self.GetSifangImageUrl('%s%d.html' %(GetUrl,self.__PageCount))
        
        if self.__PageCount != 1:        
            print '===All page[%d] has been gotten===' %self.__PageCount
            self.__PageCount = 1        
#         self.__PageCount += 1
#         if self.__PageCount > Max_Page_Num:
#             print '===page[%d] to max page===' %self.__PageCount
#             return
#         self.GetSifangImageUrl('http://www.meizitu.com/a/list_1_%d.html' %self.__PageCount)
#         
    def GetImageData(self, oneBlum):
        try:
            blumHtmlBase = self.SessionBase.get(oneBlum['url'])
        except Exception as e:
            print e
            return 
        
        blumHtmlBase.encoding = 'gb2312'
        baseSoup = BeautifulSoup(blumHtmlBase.text)
        
        albumName = baseSoup('div', {'class':"metaRight"})[0].h2.get_text()
        if os.path.exists(DirName+ albumName) == False:
                os.mkdir(DirName+ albumName)

        picDiv = baseSoup.find('div', id='picture')
#         picUrls = 
        picUrls = ''
        if picDiv == None:
            icUrls = baseSoup('div', {'class':'postContent'})[0]('img', {'class':'scrollLoading'})
        else:
            picUrls=picDiv.select('img')
        
        for img in picUrls:
            sleep(1)
            imgSrc = img['src']
            
            items = imgSrc.split('/')
            if os.path.exists(DirName+albumName+'/'+items[-1]):
                print 'this img has existed'
                sleep(1)
                continue
            
            try:
#                 print imgSrc
                imgReq = urllib2.Request(imgSrc);
                imgResp = urllib2.urlopen(imgReq);
                respHtml = imgResp.read();
            except Exception as e:
                print e
                continue
            
            imgFile = open(DirName+albumName+'/'+items[-1], "wb");
            imgFile.write(respHtml);
             
            imgFile.close();
#             try:
#                 print 'thread[%d]111111111111111111111111111111111111111111111' %(self.name)
#                 urllib.urlretrieve(imgSrc, 'img/'+str(oneBlum['num'])+'/'+items[-1])
#                 print 'urlretrieve:%d->%s' %(self.name, imgSrc)
#             except Exception as e:
#                 print e
#                 print "===>img src:%s" %imgSrc
                
# if __name__ == "__main__":
#     print 'start project'
#     reload(sys)
#     
#     if os.path.exists(DirName) == False:
#                 os.mkdir(DirName)
#                 
#     socket.setdefaulttimeout(10)
#         
# #     sys.setdefaultencoding('utf-8')
#     imageStart = Image(url=GetUrl+'1.html', name=15)
#     imageStart.GetSifangImageUrl()
#     print '===Get blums end, Start to getting image,sum[%d]===' %imageStart.AllBlumCount()
#     taskList = []
#     for i in range(15):
#         newTask = Image(name=i)
#         taskList.append(newTask)
#         newTask.start();
#         
#         
#     imageStart.start()
#     taskList.append(imageStart)
# #      
#     print '===Wait for getting image data ending==='
#     for task in taskList:
#         print "wait %s exit" %task.name
#         task.join()
#     
#     print '###Get image end'
#         
#     
#     