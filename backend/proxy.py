from lxml.html import fromstring
import requests

class Proxy:
    """Module qui permet de récupéré des liste de proxy"""
    def __init__(self):
        '''Contrructeur lance les fonctionnalité principal du programme'''
        self.proxies_list = self.get_proxies()

    def get_proxies(self):
        '''Fontionnalité de recuperation d'une liste de proxy sur free-proxy-list.net'''

        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = []
        for i in parser.xpath('//tbody/tr'):
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxies.append(":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]]))
        return proxies