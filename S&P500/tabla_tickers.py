from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import re
import json
import requests
import bs4
import urllib
import time
import csv

def get_SP_tab():

	url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

	page = urllib.request.urlopen(url).read()
	soup = bs4.BeautifulSoup(page, 'lxml')   
	tab = soup.select('table')[0].select('td')

	texto = []

	for i in tab:
		texto.append(i.text)
	texto.insert(0, ' ')

	tick = []
	comp = []
	hc = []
	div = []

	for n in range(int(len(texto)/9)):
		ind = 9*(n)
		if(ind < len(texto)):
			tick.append(texto[ind+1])
			comp.append(texto[ind+2])
			hc.append(texto[ind+6])
			div.append(texto[ind+4])

	return pd.DataFrame({'Ticker':tick, 'Compañia':comp, 'HeadCuarters':hc, 'Division':div})

def get_timestamp(fecha, dias):
#Se da timestamp1 = fecha, timestamp2 = fecha - dias

	timestamp2 = int(
					time.mktime(datetime.strptime(
										fecha.strftime("%d/%m/%Y"), "%d/%m/%Y").\
					timetuple())
					)
	timestamp1 = int(
					time.mktime(datetime.strptime(
										(fecha - timedelta(days = dias)).strftime("%d/%m/%Y"),
										 "%d/%m/%Y").\
					timetuple())
					)
	return timestamp1, timestamp2

def get_ticker_tab(tick, TS1, TS2):
#obtiene el resultado de la lectura del ticker.
#Intervalo: 1 día.

	url = 'https://query1.finance.yahoo.com/v8/finance/chart/'+tick+'?symbol='+tick+'&period1='+str(TS1)+'&period2='+str(TS2)+\
		'&interval=1d&includePrePost=true&events=div%2Csplit'

	page = str(
		urllib.request.urlopen(url).read()
		)[1:]
	page = re.sub(r"'", r"", page)

	dic = json.loads(page)['chart']['result'][0]

	return dic

def structure_table(dic):

	return df

if __name__ == '__main__':
	print('\n\t\t--- Obteniendo Tickers ---\n')
	base = get_SP_tab()
	tick = base.Ticker.tolist()
	today = datetime.now()
	TS1, TS2 = get_timestamp(today, 500)
	tickers = base.Ticker.tolist()
	
	print('\n\t   ----- Obteniendo información -----\n')

	info = get_ticker_tab(tickers[0], TS1, TS2)

	print(info)

