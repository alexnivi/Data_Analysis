import re
import pandas as pd
import bs4
import urllib


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

db = pd.DataFrame({'Ticker':tick, 'Compañia':comp, 'HeadCuarters':hc, 'Division':div})