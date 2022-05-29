import requests
from  bs4 import BeautifulSoup as bs
from random import randint
__all__ = ('hh','uzjobble','ishkop')

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    ]

def hh(url,city=None,language=None):

    jobs = []
    errors = []
    if url:
        r = requests.get(url, headers=headers[randint(0, 2)])
        if r.status_code==200:
            soup=bs(r.content,'html.parser')
            main_div=soup.find('div','sticky-container')
            if main_div:
#
                vacations=main_div.find_all('div','vacancy-serp-item')
                for vacation in vacations:
                    title_and_format=vacation.find('a','bloko-link')
                    jobs.append({
                        'url':title_and_format.get('href'),

                        'title': title_and_format.get_text(),
                        'company':vacation.find('div','vacancy-serp-item__meta-info-company').a.get_text(),

                        'description':vacation.find('div','g-user-content').get_text(),
                        'city_id':city,
                        'language_id':language




                    })

            else:
                errors.append({'url':url,'title':'main_div not exicst'})

        else:
            errors.append({'url':url,'title':'Page do not response'})

    return jobs,errors


def uzjobble(url,city=None,language=None):
    jobs = []
    errors = []
    if url:
        r = requests.get(url, headers=headers[randint(0, 2)])

        if r.status_code==200:
            soup=bs(r.content,'html.parser')
            # with open('parsering.html','w') as file:
            #     file.write(str(soup))




            vacations=soup.find_all('article','yKsady')

            print(vacations,'1111111111')

            for vacation in vacations:



                jobs.append({
                    'url':vacation.find_next('a').get('href'),

                    'title': vacation.find('span','_33bQdO').get_text(),
                    'company':vacation.find('p','Ya0gV9').get_text(),

                    'description':vacation.find('div','_9jGwm1').get_text(),
                    'city_id':city,
                    'language_id':language




                })


    return jobs,errors


def ishkop(url,city=None,language=None):
    total_url='https://ishkop.uz/viewjob?'
    jobs = []
    errors = []
    if url:
        r = requests.get(url, headers=headers[randint(0, 2)])
        if r.status_code==200:
            soup=bs(r.content,'html.parser')
            main_div=soup.find('div','jobs')
            if main_div:

                 vacations=main_div.find_all('article','job no-logo')
                 for vacation in vacations:
                     title_and_url=vacation.find('h2','title').find_next('a')


                     jobs.append({
                        'url':total_url+title_and_url.get('href'),

                        'title': title_and_url.get_text(),
                        'company':vacation.find('div','company-job-data').get_text(),

                        'description':vacation.find('div','desc').get_text(),
                        'city_id':city,
                        'language_id':language




                    })

    return jobs,errors
# urlhh='https://tashkent.hh.uz/search/vacancy?clusters=true&area=2759&ored_clusters=true&order_by=publication_time&enable_snippets=true&salary=&st=searchVacancy&text=python'
# urlishkop="https://ishkop.uz/vacansii?q=python&l=Ташкент&df=3"
# urluzjobble="https://uz.jooble.org/SearchResult?p=4&rgns=Ташкент&ukw=python"
# h=hh(urlhh)
# ish=ishkop(urlishkop)
# uzjobble(urluzjobble)

