import requests
from datetime import datetime

def download_expenses():
    base_url = 'https://www.camara.leg.br/cotas/Ano-{year}.csv.zip'
    starting_year = 2008
    current_year = datetime.now().year;

    for i in range(starting_year, current_year + 1):
        print(base_url.format(year = i))
        #download_response = requests.get(base_url.format(year = i), stream=True)
        
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }        

        response = requests.get(base_url.format(year = i), headers=headers, stream=True)
        
        if response.status_code == 200:
            with open(f"Ano-{i}.csv.zip", "wb") as csv_file:
                for chunk in response.iter_content(chunk_size=1024):
                    csv_file.write(chunk)
            print(f"Download successful!")
        else:
            print(f"Download error: {response.status_code} - {response.text}")
    
if __name__ == '__main__':
    download_expenses()