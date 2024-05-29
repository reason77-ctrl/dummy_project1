from requests_html import HTMLSession
import json

url = 'https://www.laliga.com/en-GB/laliga-easports/standing'

s = HTMLSession()

def get_url(url):
    
    r = s.get(url)
    return r


def get_table():
    r = get_url(url)
    table = r.html.find('.show')[0]

    table_data = [[c.text for c in row.find('.styled__TextStyled-sc-1mby3k1-0')[2:]] for row in table.find('.styled__StandingTabBody-sc-e89col-0')]

    table_header = [[c.text for c in row.find('.styled__TextStyled-sc-1mby3k1-0')[1:]] for row in table.find('.styled__StandingTabHeader-sc-e89col-7')][0]

    result = [dict(zip(table_header, t)) for t in table_data]

    return result

def json_convert():
    result = get_table()
    with open('table.json', 'w') as data_file:
        a = json.dump(result, data_file, indent=2)
    return a


