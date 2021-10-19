import codecs
from bs4 import BeautifulSoup as BS
import requests


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}




jobs = []
errors = []


def work_parser(url):

    domain = 'https://www.work.ua'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id="pjax-job-list")
        if main_div:
            div_list = main_div.find_all('div', attrs={'class': 'job-link'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                description = div.p.text

                logo = div.find('img')
                if logo:
                    company = logo['alt']
                else:
                    company = 'No name'

                       #ключи в словаре - поля модели Vacancy (models.py): значения - это переменные описанные выше
                jobs.append({'title': title.text, 'url': domain+href, 'description': description, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exist'})

    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


url = 'https://www.work.ua/ru/jobs-kyiv-python/'
work_parser(url)

file = codecs.open('work.txt', 'w', 'utf-8') #windows-1251 иногда вместо utf-8
file.write(str(jobs))
file.close()





#file = codecs.open('work.html', 'w', 'utf-8') #windows-1251 иногда вместо utf-8
#file.write(str(resp.text))
#file.close()

