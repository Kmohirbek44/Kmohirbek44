import asyncio
import os, sys

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'API_project.settings'
import django

django.setup()
import scraping.models
from scraping.parsers import *

parser = (
    (hh, 'hh'),
    (ishkop, 'ishkop'),
    (uzjobble, 'uzjobble'),

)
jobs, errors = [], []

User = get_user_model()


def get_user():
    qs = User.objects.filter(send_email=True).values()
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst


def get_urls(_settings):
    qs = scraping.models.Urls.objects.all().values()
    dict_url = {(q['city_id'], q['language_id']): q['data'] for q in qs}
    urls = []
    for pair in _settings:
        tmp = {}
        tmp['city'] = pair[0]
        tmp['language'] = pair[1]
        tmp['data'] = dict_url[pair]
        urls.append(tmp)
    return urls


async def main(value):
    func, url, city, language = value
    job, err = await loop.run_in_executor(None, func, url, city, language)
    jobs.extend(job)
    errors.extend(err)


a = get_user()
get_url = get_urls(a)
loop = asyncio.get_event_loop()
tmp_tasks = [(func, data['data'][key], data['city'], data['language'])
             for data in get_url for func, key in parser]
tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])
loop.run_until_complete(tasks)
loop.close()
for job in jobs:

    v = scraping.models.Vakation(**job)
    try:
        v.save()
    except DatabaseError:
        v.save()

# from send_email import send
#
# send()
