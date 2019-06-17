from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup

# Create your views here.
lst=[

]

content = {

}

def home(request):
    global lst
    global content
    return render(request,'todolist/home.html',content)

def about(request):
    return render(request,'todolist/about.html')

def suibi(request):
    global lst
    global content
    lst.clear()
    content.clear()

    #爬虫程序
    res = requests.get("https://www.douban.com/tag/%E9%9A%8F%E7%AC%94/?source=related")
    soup = BeautifulSoup(res.text,"lxml")
    book_div = soup.find(attrs={"id":"book"})
    #标题
    book_a = book_div.findAll(attrs={"class":"title"})
    #图片链接
    book_img = book_div.findAll('img')

    for i in range(9):
        lst.append({'title':book_a[i].string,'img':book_img[i].get('src')})
    
    content= {'清单':lst,'信息':'爬取随笔成功'}
    return redirect('todolist:主页')

def shige(request):
    global lst
    global content
    lst.clear()
    content.clear()

    #爬虫程序
    res = requests.get("https://www.douban.com/tag/%E8%AF%97%E6%AD%8C/?source=related")
    soup = BeautifulSoup(res.text,"lxml")
    book_div = soup.find(attrs={"id":"book"})
    #标题
    book_a = book_div.findAll(attrs={"class":"title"})
    #图片链接
    book_img = book_div.findAll('img')
    
    for i in range(9):
        lst.append({'title':book_a[i].string,'img':book_img[i].get('src')})
    
    content= {'清单':lst,'信息':'爬取诗歌成功'}
    return redirect('todolist:主页')

def xiaoshuo(request):
    global lst
    global content
    lst.clear()
    content.clear()

    #爬虫程序
    res = requests.get("https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?source=related")
    soup = BeautifulSoup(res.text,"lxml")
    book_div = soup.find(attrs={"id":"book"})
    #标题
    book_a = book_div.findAll(attrs={"class":"title"})
    #图片链接
    book_img = book_div.findAll('img')
   
    for i in range(9):
        lst.append({'title':book_a[i].string,'img':book_img[i].get('src')})
    
    content= {'清单':lst,'信息':'爬取小说成功'}
    return redirect('todolist:主页')