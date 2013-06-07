#Name: stock-extractor.py
#Author: Karambir Singh Nain

import requests
from BeautifulSoup import BeautifulSoup

def data_extractor(base_url):
    r = requests.get(base_url)
    html = BeautifulSoup(r.content)

    #print html.prettify()
    all_tables = html.findAll('table')
    #print len(all_tables)
    data = all_tables[-2]
    #print data.findAll('tr')
    years = []
    for year in data.tr.findAll('td'):
        if len(year.text)>3:
            years.append(year.text.replace("'", ""))
    total_income = []
    net_profit = []
    for row in data:
        try:
            if 'Total Income' in row.td.text:
                for nums in row.findAll('td'):
                    try:
                        total_income.append(float(nums.text.replace(',', '')))
                    except ValueError:
                        pass
                print 'Total Income Found'
            if 'Reported Net Profit' in row.td.text:
                for nums in row.findAll('td'):
                    try:
                        net_profit.append(float(nums.text.replace(',', '')))
                    except ValueError:
                        pass
                print 'Net Profit Found'
        except AttributeError:
            pass
    print total_income
    print net_profit
    print years
    #result = {}
    #for year, nums in zip(years.findAll('td'), income.findAll('td')):
    #    #print year.text, nums.text
    #    if 'Total Income' not in nums.text:
    #        result[year.text] = float(nums.text.replace(',', ''))
    #print result
    #print years
    #print income

def main():
    print "=" * 50
    print "Stock extractor"
    print "=" * 50
    base_url = raw_input("Give stock url: ")

    data_extractor(base_url)


if __name__ == '__main__':
    main()
