#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import  urllib
import re
import handle_Single_Html

# f2 = open('ProgramLeader_content.txt','w+')

str_url ='http://blog.csdn.net/for5million/article/category/5588287/'

def getLink(url):
    f1 = open('ProgramLeader_link.txt','w+')
    for i in range(1,4) :
        body = ''
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
        headers = { 'User-Agent' : user_agent }
        str_use = url + str(i)
        request = urllib2.Request(str_use,body,headers)
        response = urllib2.urlopen(request)
        html =response.read()
        # reg = r'<span class="link_title"><a href="(.+?)">'
        pattern = re.compile('<span class="link_title"><a href="(.*?)">',re.S)

        content = re.findall(pattern,html)
        # print type(content)
        # content.reverse()
        for title_Link_writeIn in content:
            f1.writelines('http://blog.csdn.net'+str(title_Link_writeIn)+'\n')
    f1.close()
#翻转链接
def reverse_Link():
    f1 = open('ProgramLeader_link.txt','r')
    content = f1.readlines()
    content.reverse()
    f1.close()
    # f1 = open('ProgramLeader_link.txt','w')
    # f1.truncate()
    f1 = open('ProgramLeader_link.txt','w')
    for item in content:
        f1.writelines(item)
    f1.close()

# def get_Content():
#     content_link = f1.readlines()
#     for i in content_link:
#         Link_url = i.strip()
#         body = ''
#         user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
#         headers = { 'User-Agent' : user_agent }
#         str_use = Link_url
#         request = urllib2.Request(str_use,body,headers)
#         response = urllib2.urlopen(request)
#         html =response.read()

def get_Content():
    f1 = open('ProgramLeader_link.txt')
    Link = f1.readline()
    print Link
    while Link :
        handle_Single_Html.write_In(Link)
        handle_Single_Html.extract_Html()
        Link = f1.readline()
    f1.close()
getLink(str_url)
reverse_Link()
# reverse_Link()
get_Content()
# handle_Single_Html.f1.close()
# handle_Single_Html.f2.close()
# pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
#         #个人信息页面所有代码
#         content = re.search(pattern,page)
#         #从代码中提取图片
#         patternImg = re.compile('<img.*?src="(.*?)"',re.S)
#         images = re.findall(patternImg,content.group(1))
#         return images

# url = 'http://www.baidu.com'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }
# data = urllib.urlencode(values)
# req = urllib2.Request(url,  headers)
# response = urllib2.urlopen(req)
# the_page = response.read()

 # def getPage(self,pageIndex):
 #        url = self.siteURL + "?page=" + str(pageIndex)
 #        print url
 #        request = urllib2.Request(url)
 #        response = urllib2.urlopen(request)
 #        return response.read().decode('gbk')
 #
 #    def getContents(self,pageIndex):
 #        page = self.getPage(pageIndex)
 #        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
 #        items = re.findall(pattern,page)
 #        for item in items:
 #            print item[0],item[1],item[2],item[3],item[4]
