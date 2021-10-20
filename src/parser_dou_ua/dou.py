import codecs
from bs4 import BeautifulSoup as BS
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}




jobs = []
errors = []

def dou_parser(url):

    #domain = 'https://jobs.dou.ua'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id="vacancyListId")

        if main_div:
            li_list_hot = main_div.find_all('li', attrs={'class': 'l-vacancy __hot'})
            li_list = main_div.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_list:
                title = li.find('div', attrs={'class': 'title'})
                href = title.a['href']
                desc = li.find('div', attrs={'class': 'sh-info'})
                description = desc.text

                company = 'No name'
                a = title.find('a', attrs={'class': 'company'})
                if a:
                    company = a.text

                       #ключи в словаре - поля модели Vacancy (models.py): значения - это переменные описанные выше
                jobs.append({'title': title.text, 'url': href, 'description': description, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Table does not exist'})

    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors

#--------------------------------------------------------------------------------------------------------------------------
#url = 'https://jobs.dou.ua/vacancies/?city=Київ&search=Python'
#dou_parser(url)

#file = codecs.open('parser_dou_ua/dou.txt', 'w', 'utf-8') #windows-1251 иногда вместо utf-8
#file.write(str(jobs))
#file.close()