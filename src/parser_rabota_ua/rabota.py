import codecs
from bs4 import BeautifulSoup as BS
import requests


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.362',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}




jobs = []
errors = []

def rabota_parser(url):

    domain = 'https://rabota.ua'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        table = soup.find('table', id="ctl00_content_vacancyList_gridList")

        if table:
            tr_list = table.find_all('tr', attrs={'id': True}) # True - если полей с id много и они все уникальные и они все типа как нужны
            for tr in tr_list:
                div = tr.find('div', attrs={'class': 'card-body'})
                if div:
                    title = div.find('h2', attrs={'class': 'card-title'})
                    href = title.a['href']
                    desc = tr.find('div', attrs={'class': 'card-description'})
                    description = desc.text

                a = div.find('a', attrs={'class': 'company-profile-name'})
                company = 'No name'
                if a:
                    company = a.text

                       #ключи в словаре - поля модели Vacancy (models.py): значения - это переменные описанные выше
                jobs.append({'title': title.text, 'url': domain+href, 'description': description, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Table does not exist'})

    else:
        errors.append({'url': url, 'title': 'Page do not response'})

url = 'https://rabota.ua/zapros/python/киев'
rabota_parser(url)

file = codecs.open('rabota.txt', 'w', 'utf-8') #windows-1251 иногда вместо utf-8
file.write(str(jobs))
file.close()