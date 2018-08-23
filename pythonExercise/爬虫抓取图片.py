# -*- coding:utf-8 -*-
import time
from urllib import request
from bs4 import BeautifulSoup
import re

url = r'https://www.zhihu.com/question/22918070'
headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')

# Beautiful Soup和正则表达式结合，提取出所有图片的链接（img标签中，class=**，以.jpg结尾的链接）
links = soup.find_all(
    'img', "origin_image zh-lightbox-thumb", src=re.compile(r'.jpg$'))
# 设置保存的路径，否则会保存到程序当前路径
local_path = r'F:\VScode\pythonExercise\Pic'

for link in links:
    print(link.attrs['src'])
    # 保存链接并命名，time防止命名冲突
    request.urlretrieve(link.attrs['src'], local_path+r'\%s.jpg' % time.time())
