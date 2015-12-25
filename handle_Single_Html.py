#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import chardet


def write_In(Single_html):
#将单独的网页提取出来写入文件进行分析
    f1 = open('Html_content.html','w')
    f2 = open('Html_content.txt','a')
    f3 = open('Html_content_Sum.html','a')
    str_use = Single_html
    body = ''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(str_use,body,headers)
    response = urllib2.urlopen(request)
    html =response.read()
    # assert isinstance(html_white, object)
    # html = chardet.detect(html_white)
    soup = BeautifulSoup(html)
    # print soup.prettify()#article_content
    title = soup.title.string.encode('utf')
    # # print type(title)切片操作
    # title_split = []
    # title_split = title.split('-')
    # title_split = title_split[0:2]
    # print title_split
    # title = "-".join(title_split)
    # title = title_split.join(title_split[0:1])错误代码
    f2.write('---------------------------------------------------\n'+ title + '\n'+'---------------------------------------------------\n')
    f3.write('\n---------------------------------------------------\n'+ '<p style="margin-top:0px; margin-bottom:15px; color:rgb(51,51,51); font-family:Tahoma,Helvetica,Arial,sans-serif; font-size:14px; letter-spacing:0.5px; line-height:24px">'+ title + '</p>' + '\n'+'---------------------------------------------------\n')
# <p style="margin-top:0px; margin-bottom:15px; color:rgb(51,51,51); font-family:Tahoma,Helvetica,Arial,sans-serif; font-size:14px; letter-spacing:0.5px; line-height:24px">
# 从事it工作10余年，痛并快乐着。</p>
    content = soup.find_all(id="article_content")

    for item in content:
        # item = chardet.detect(item)
        f1.write(str(item))
        f3.write(str(item))
    f1.close()
    f2.close()
    f3.close()


def extract_Html():
    f1 = open('Html_content.html')
    f2 = open('Html_content.txt','a')
    # print open('Html_content.html').read()
    # print "-------------------------------------"
    # f1.close()
    html_finish = BeautifulSoup(f1.read(),from_encoding="gb18030")
    # print html_finish
    content_finish = html_finish.stripped_strings

    for item in content_finish:
        f2.write(item.encode('utf')+'\n')
        # print item
    f1.close()
    f2.close()

# write_In('http://blog.csdn.net/for5million/article/details/47154311')
# extract_Html()