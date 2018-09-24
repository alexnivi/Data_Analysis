#!/bin/bash

if [ ! -d data ]; then
	echo "\n\t---- No existen datos históricos ----"
	mkdir data
	python tabla_tickers.py
fi