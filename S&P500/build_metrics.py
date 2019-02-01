import pandas as pd
import numpy as np
import joblib

def lag_Data(dat, periods = 5):
	
	lagged_dat = dat.copy(deep=True)

	for i in range(1,periods+1):
		tab = (dat.shift(i)).drop('date', axis=1)
		tab.columns = ['ticker_'+str(i), 'open_'+str(i), 'high_'+str(i), 'low_'+str(i), 
					'close_'+str(i), 'volume_'+str(i)]
		lagged_dat = pd.concat([lagged_dat, tab], axis = 1)
	
	lagged_dat = lagged_dat.loc[(-pd.isna(lagged_dat['high_' + str(i)])) & 
				(lagged_dat.ticker == lagged_dat['ticker_' + str(i)])]
	for i in range(1,periods+1):
		lagged_dat = lagged_dat.drop('ticker_'+str(i), axis = 1)

	return lagged_dat, periods

def get_yield(dat, periods):
		for i in range(1,periods+1):
			dat['yield_'+str(i)] = dat['close_'+str(i)-'open_'+str(i)]


if __name__ == '__main__':

	dat = joblib.load('data/BaseS&P500.pkl')
	met, periods = lag_Data(dat, 6)
	

	tickers = list(dat.ticker)
	dat = dat.gorupby(['ticker', 'date'])
	print('\n\t    --- Cargando Datos Anteriores ---\n')