from bs4 import BeautifulSoup
import requests
import os
usr_input = str(input('Digite a série: '))
def get_tpb(search_query):#Procura na página do tpb
    search_query = search_query.replace(" ", "%20").replace("'", '')
    down_source = requests.get('https://thepiratebay.org/search/' + search_query).text
    down_soup = BeautifulSoup(down_source, "html5lib")
    return down_soup
def Main():
    source = requests.get('http://www.airdates.tv/#today').text
    soup = BeautifulSoup(source, "html5lib")
    #Busca a Semana
    for each_day in soup.find_all('div', class_='day past'):
        date_week = each_day.find('div', class_="date").text
        #Busca em cada semana as Séries com Episódeos
        for each_show in each_day.find_all('div' , class_='title'):
            if usr_input in each_show.text:
                print('\n' + '=== ' + date_week + ' ===' + '\n')
                print('- '+each_show.text)
                name = each_show.text
                query_results= get_tpb(name)
                if query_results.find('a', title='Download this torrent using magnet') is None:
                    print('Não há link de Download/Não foi lançado')
                else:
                    down_mag = query_results.find('a', title='Download this torrent using magnet')['href']
                    seeders = query_results.find('td',align='right').text
                    print(down_mag + '\n' + 'Seeders: ' + seeders)
    os.system("pause")
Main()
