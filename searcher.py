from bs4 import BeautifulSoup
import requests
import os
text_file = open("Output.txt", "w")

usr_input = str(input('Show Name: '))
def get_tpb(search_query):#Procura na página do tpb
    search_query = search_query.replace(" ", "%20").replace("'", '')
    down_source = requests.get('https://thepiratebay.org/search/' + search_query).text
    down_soup = BeautifulSoup(down_source, "html5lib")
    return down_soup
def Main():
    source = requests.get('http://www.airdates.tv/').text
    soup = BeautifulSoup(source, "html5lib")
    #print(soup.prettify())
    text_file.write(str(soup))
    text_file.close()
    
    #Busca a Semana
    #Para dias anteriores ao Atual
    for each_day in soup.find_all('div', class_='day past'):
        date_week = each_day.find('div', class_="date").text
        #Busca em cada semana as Séries com Episódios
        for each_show in each_day.find_all('div' , class_='title'):
            if usr_input in each_show.text:
                print('\n' + '=== ' + date_week + ' ===' + '\n')
                print('- '+each_show.text)
                name = each_show.text
                query_results= get_tpb(name)
                if query_results.find('a', title='Download this torrent using magnet') is None:
                    print('Not Released yet/No Download link')
                else:
                    down_mag = query_results.find('a', title='Download this torrent using magnet')['href']
                    seeders = query_results.find('td',align='right').text
                    print(down_mag + '\n' + 'Seeders: ' + seeders)
    # Para Dias Após o atual
    for each_day in soup.find_all('div', class_='day'):
        date_week = each_day.find('div', class_="date").text
        #Busca em cada semana as Séries com Episódios
        for each_show in each_day.find_all('div' , class_='title'):
            if usr_input in each_show.text:
                print('\n' + '=== ' + date_week + ' ===' + '\n')
                print('- '+each_show.text)
                name = each_show.text
                query_results= get_tpb(name)
                if query_results.find('a', title='Download this torrent using magnet') is None:
                    print('Not Released yet/No Download link')
                else:
                    down_mag = query_results.find('a', title='Download this torrent using magnet')['href']
                    seeders = query_results.find('td',align='right').text
                    print(down_mag + '\n' + 'Seeders: ' + seeders)
        
    os.system("pause")
Main()
