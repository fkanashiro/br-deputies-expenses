import requests
from datetime import datetime

def download_expenses():
    base_url = 'https://www.camara.leg.br/cotas/Ano-{year}.csv.zip'
    starting_year = 2008
    current_year = datetime.now().year;

    for i in range(starting_year, current_year + 1):
        print(base_url.format(year = i))
        download_response = requests.get(base_url.format(year = i), stream=True)
        
        with open('Ano-{year}.csv.zip'.format(year = i), 'wb') as csv_file:
            for chunk in download_response.iter_content(chunk_size=8192):
                csv_file.write(chunk)
    
download_expenses()