from user import f
import requests
from bs4 import BeautifulSoup
import lxml
from random import choice
import json


def get_html(url, proxy=None, ua=None):
   r = requests.get(url, headers=ua, proxies=proxy)
   return r.text

def get_data(html):
   soup = BeautifulSoup(html, 'lxml')
   pogoda = soup.find('span', class_='unit unit_temperature_c').text.strip()
   with open('pog.json', 'w') as file:
      json.dump(pogoda,file)


def dyurtyuli():
   url = 'https://www.gismeteo.ru/weather-dyurtyuli-4555/'

   useragents = open('ua.txt').read().split('\n')
   proxies = open('proxies.txt').read().split('\n')

   proxy = {'http': 'http://' + choice(proxies)}
   usag = {'User-Agent': choice(useragents)}
   
   html = get_html(url, proxy, usag)
   get_data(html)

def ufa():
   url = 'https://www.gismeteo.ru/weather-ufa-4588/'

   useragents = open('ua.txt').read().split('\n')
   proxies = open('proxies.txt').read().split('\n')

   proxy = {'http': 'http://' + choice(proxies)}
   usag = {'User-Agent': choice(useragents)}
   
   html = get_html(url, proxy, usag)
   get_data(html)

def yekaterinburg():
   url = 'https://www.gismeteo.ru/weather-yekaterinburg-4517/'

   useragents = open('ua.txt').read().split('\n')
   proxies = open('proxies.txt').read().split('\n')

   proxy = {'http': 'http://' + choice(proxies)}
   usag = {'User-Agent': choice(useragents)}
   
   html = get_html(url, proxy, usag)
   get_data(html)

def moscow():
   url = 'https://www.gismeteo.ru/weather-moscow-4368/'

   useragents = open('ua.txt').read().split('\n')
   proxies = open('proxies.txt').read().split('\n')

   proxy = {'http': 'http://' + choice(proxies)}
   usag = {'User-Agent': choice(useragents)}
   
   html = get_html(url, proxy, usag)
   get_data(html)

def kazan():
   url = 'https://www.gismeteo.ru/weather-kazan-4364/'

   useragents = open('ua.txt').read().split('\n')
   proxies = open('proxies.txt').read().split('\n')

   proxy = {'http': 'http://' + choice(proxies)}
   usag = {'User-Agent': choice(useragents)}
   
   html = get_html(url, proxy, usag)
   get_data(html)

def saint_peterburg():
   url = 'https://www.gismeteo.ru/weather-sankt-peterburg-4079/'

   useragents = open('ua.txt').read().split('\n')
   proxies = open('proxies.txt').read().split('\n')

   proxy = {'http': 'http://' + choice(proxies)}
   usag = {'User-Agent': choice(useragents)}
   
   html = get_html(url, proxy, usag)
   get_data(html)


