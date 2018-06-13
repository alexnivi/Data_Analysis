import pandas as pd
import numpy as np
import requests
import bs4
import sys

def get_page(url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'):

	try:
		pag = requests.get(url)
	except ValueError:
		print("URL not a web page. Try again...")
		return 0

	

	if pag.status_code == 200:
		print('URL ok, se extrae la info')
		text = pag.text
	else: 
		print(pag + 'URL ERROR, sin info')
		text = 0

	return text

if __name__ == "__main__":
   
	url = sys.argv

	if len(url) == 2:
		text = get_page(url)
	else:
		text = get_page()

	print(text)

   #text = gat_page(url)


