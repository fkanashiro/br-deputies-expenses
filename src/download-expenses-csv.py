import requests
from datetime import datetime

def download_expenses():
    base_url = 'https://www.camara.leg.br/cotas/Ano-{year}.csv.zip'
    starting_year = 2008
    current_year = datetime.now().year;

    for i in range(starting_year, current_year + 1):
        print(base_url.format(year = i))
    
download_expenses()