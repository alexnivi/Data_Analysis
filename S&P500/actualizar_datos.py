import re
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from tabla_tickers import get_timestamp, get_ticker_tab, get_SP_tab, structure_table
import os

def lista_tickers():
	if 'Tablatickers.pkl' in os.listdir("data"):
		tab_tick = joblib.load('data/Tablatickers.pkl')
	else:
		tab_tick = get_SP_tab()
		joblib.dump(tab_tick, 'data/Tablatickers.pkl')

	tickers = tab_tick.Ticker.tolist()
	tickers = [re.sub(r"\.", r"-", i) for i in tickers]

	return tickers

def obtener_tabla_datos(tickers):
	db = pd.DataFrame()
	ind = 0
	tot = len(tickers)

	for i in tickers:
		ind +=1
		dic = get_ticker_tab(i, TS1, TS2)
		db = pd.concat([db, structure_table(dic)])
		print(str(ind) + ' de ' + str(tot) + ' --- ' + i + ' check!')

	return db


if __name__ == '__main__':
	print('\n\t    --- Cargando Datos Anteriores ---\n')
	base = joblib.load('data/BaseS&P500.pkl')
	last_date = np.max(base.date)
	today = datetime.now()
	days = (today - last_date).days + 5
	TS1, TS2 = get_timestamp(today, days)
	tickers = lista_tickers()

	print('\n\t    ----- Actualizando Información -----\n')

	db = obtener_tabla_datos(tickers)
	anterior = joblib.load('data/BaseS&P500.pkl')
	nueva = pd.concat([anterior, db]).sort_values(['ticker', 'date']).drop_duplicates().reset_index(drop=True)

	joblib.dump(nueva, 'data/BaseS&P500.pkl')