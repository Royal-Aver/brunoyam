# Уровень 1 и 2:
import time
from _datetime import datetime
from threading import Thread

thread_name = ['name1', 'name2', 'name3', 'name4', 'name5']

current_time = datetime.now()

def get_thread(thread_name):
    time.sleep(1)
    print(f'вывожу {thread_name} за {(datetime.now() - current_time).microseconds}')

threads = [Thread(target=get_thread, args=(thread_name[i], )) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()


for i in range(5):  # последовательный запуск
    get_thread(thread_name[i])


# Уровень 3:
import requests

links = ['https://www.google.ru/?hl=ru', 'https://www.apple.com/ru/mac/', 'https://www.bk.com/',
         'https://www.avito.ru/', 'https://www.aviasales.ru/']

def get_html(link):
    requests.get(link)
    print(f'получил информацию с сайта {link} за {(datetime.now() - current_time).microseconds} миллисекунд')

req = [Thread(target=get_html, args=(links[i], )) for i in range(5)]

for r in req:
    r.start()

for r in req:
    r.join()

for i in range(5):
    get_html(links[i])
