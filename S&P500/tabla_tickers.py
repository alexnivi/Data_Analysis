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
import joblib

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

	db = pd.DataFrame.from_dict(dic['indicators']['quote'][0])
	tmstmp = dic['timestamp']
	tmstmp = [datetime.strptime(time.strftime("%d/%b/%Y", time.localtime(int(x))), "%d/%b/%Y") for x in tmstmp]
	db['date'] = tmstmp
	db['ticker'] = dic['meta']['symbol']
	db = db[['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']]

	return db

if __name__ == '__main__':
	print('\n\t\t--- Obteniendo Tickers ---\n')
	base = get_SP_tab()
	tickers = base.Ticker.tolist()
	tickers = [re.sub(r"\.", r"-", i) for i in tickers]
	today = datetime.now()
	TS1, TS2 = get_timestamp(today, 950)
	
	print('\n\t    ----- Obteniendo Información -----\n')

	db = pd.DataFrame()

	ind = 0
	tot = len(tickers)

	for i in tickers:

		ind +=1
		dic = get_ticker_tab(i, TS1, TS2)
		db = pd.concat([db, structure_table(dic)])
		print(str(ind) + ' de ' + str(tot) + ' --- ' + i + ' check!')

	joblib.dump(db, 'BaseS&P500.pkl')
	print('\n\t\t    ----- Done! -----\n')