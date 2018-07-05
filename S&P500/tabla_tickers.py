from datetime import datetime
import re
import pandas as pd
import bs4
import urllib

def get_SP_tab()

	url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

	page = urllib.request.urlopen(url).read()
	soup = bs4.BeautifulSoup(page)   
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

def get_timestamp(fecha):
	tme = datetime.strptime('20.12.2016 09:38:42,76',
                           '%d.%m.%Y %H:%M:%S,%f')


def get_ticker_info(ticker, fecha_inicio, fecha_fin):
	#Se obtiene información diaria de la acción

	url = https://query1.finance.yahoo.com/v7/finance/download/ORCL?period1=1496552400&period2=1528088400&interval=1d&events=history&crumb=pJOrJOlKwNZ

if __name__ == '__main__':
	print(Obteniendo Tickers)
	base = get_SP_tab()
	tick = tab.Ticker.tolist()
	timestamp2 = datetime.datetime.now().timestamp()
