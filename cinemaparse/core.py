'''Cinema module'''
import requests
from bs4 import BeautifulSoup
class CinemaParser:
    '''class'''
    def __init__(self, city='msk'):
        ''' Узнаём город'''
        self.city = city
        self.content = ''
    def extract_raw_content(self):
        '''скачивает Html'''
        url = 'https://{}.subscity.ru'.format(self.city)
        self.content = requests.get(url)
    def print_raw_content(self):
        '''Красивый вывод HTML'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        return soup.prettify()
