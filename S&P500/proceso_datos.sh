#!/bin/bash

if [ ! -d data ]; then
	echo "\n\t---- No existen datos históricos ----"
	mkdir data
	python tabla_tickers.py
fi

if [ ! -f data/BaseS\&P500.pkl ]; then
	echo "\n\t---- No existen datos históricos ----"
	python tabla_tickers.py	
fi

if [  -f data/BaseS\&P500.pkl ]; then
	echo "\n\t---- Actualizando datos históricos ----"
	python actualizar_datos.py
fi

