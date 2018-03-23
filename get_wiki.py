
import vk
import lxml.html
import requests
from bs4 import BeautifulSoup as BS
import csv
import re
session = vk.Session('128669881286698812866988d212e793301128612866988483296fd3d6372fd5d7f2926')#6421176', 'c12021942@yandex.ru', '105150r', scope='pages, likes')
# -*- coding: utf-8 -*-
vk_api = vk.API(session)

owners = [23696820, 34215577, 77270571, 91933860]

with open('pages.csv', 'a', newline='') as csvfile:
    fieldnames = ['article', 'likes', 'watches']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    #writer.writeheader()
    for i in range(1, 1000):
        for owner in owners:
            wall = vk_api.wall.get(owner_id=-owner,offset=100*i, count=100, v='5.73')
            for iter in wall['items']:
                #f = requests.get("https://vk.com/habr?w=wall-" + str(owner) + "_" + str(iter))
                '''
                root = BS(f.text, 'lxml')
                try:
                    likes = root].find('span', {'class': 'like_people_text'}).text
                    article = root.find('div', {'class': 'pi_text'}).text
                    watches = root.find('b', {'class': 'v_views'}).text
                except AttributeError:
                    continue
                '''
                try:
                    likes = iter['likes']['count']
                    article = iter['text']
                    watches = iter['views']['count']
                    
                    article = re.sub('[^.,:;\-\"\"\'\'()! А-Яа-яA-Za-z0-9]', '', article)
                    writer.writerow({'article' : article, 'likes' : str(likes), 'watches' : str(watches)})
                except KeyError:
                    break
            

        
        


#article = vk_api.pages.get(owner_id=-owner, page_id=page, v='5.73', need_html= 1)

#html = article['html']
#res = lxml.html.document_fromstring(html).text_content()

