import json
import requests
from bs4 import BeautifulSoup
from web_scrapper_handlers.extract_table_data import get_team_from_table_row


URL = 'https://lpf.ro/liga-1'

if __name__ == '__main__':
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='html.parser')
    # print('soup', soup)

    table = soup.find('div', {'id': 'clasament_ajax'}).find('table')
    # print(table)

    table_rows = table.findAll('tr', {'class': 'echipa_row'})
    # print('table_rows', len(table_rows), table_rows)

    teams = list(map(get_team_from_table_row, table_rows))
    print('teams', list(teams))

    with open('rou_table.json', 'w+') as json_file:
        json.dump(teams, json_file)
