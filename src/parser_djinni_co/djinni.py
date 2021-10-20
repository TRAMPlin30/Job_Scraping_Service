import codecs
from bs4 import BeautifulSoup as BS
import requests


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}




jobs = []
errors = []

def djinni_parser(url):

    domain = 'https://djinni.co/jobs'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_ul = soup.find('ul', attrs={'class': 'list-unstyled list-jobs'})
        if main_ul:
            li_list = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
            for li in li_list:
                title = li.find('div', attrs={'class': 'list-jobs__title'})
                href = title.a['href']
                desc = li.find('div', attrs={'class': 'list-jobs__description'})
                description = desc.p.text

                company = 'No name'
                comp = li.find('div', attrs={'class': 'list-jobs__details__info'})
                if comp:
                    company = comp.text

                       #ключи в словаре - поля модели Vacancy (models.py): значения - это переменные описанные выше
                jobs.append({'title': title.text, 'url': domain+href, 'description': description, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Main_ul does not exist'})

    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors

#--------------------------------------------------------------------------------------------------------------------------
#url = 'https://djinni.co/jobs/location-kyiv/?keywords=Python'
#djinni_parser(url)

#file = codecs.open('parser_djinni_co/djinni.txt', 'w', 'utf-8') #windows-1251 иногда вместо utf-8
#file.write(str(jobs))
#file.close()