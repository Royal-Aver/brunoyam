import requests
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt

get_site_data = requests.get('https://mfd.ru/currency/?currency=USD')

page_text = soup(get_site_data.text, 'html.parser')

list_table = page_text.find('table', {'class': 'mfd-table mfd-currency-table'}).find_all('td')

len_list = len(list_table)

list_daily_exchange_rates = []
i = 1
while i < len_list:
    list_daily_exchange_rates.append(float(list_table[i].text))
    i += 3

amount_days = range(1, 131)

plt.title('Dollar to ruble exchange rate')
plt.xlabel('days')
plt.ylabel('rub / $')
plt.plot(amount_days, list_daily_exchange_rates)
plt.show()
