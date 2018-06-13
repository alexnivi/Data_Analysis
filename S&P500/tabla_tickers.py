import pandas as pd
import numpy as np
import requests
import bs4
import sys

def get_page(url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

	pag = requests.get(url)

if page.status_code==200:
	print('URL ok, se extrae la info')
	text = pag.text
else:
	print(pag + 'URL ERROR, sin info')
	text = 0;

return text

if __name__ == "__main__":
   
   url = sys.argv
   print(url)

   #text = gat_page(url)


