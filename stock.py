#Name: stock-extractor.py
#Author: Karambir Singh Nain

import requests
from BeautifulSoup import BeautifulSoup

def make_pretty(info):
    if 'years' in info:
        print 'working...'
        years = info['years']
        del info['years']
        pretty_info = {}
        for number, year in enumerate(years):
            pretty_info[year] = {}
            for k, v in info.iteritems():
                pretty_info[year][k] = v[number]
        return pretty_info
    else:
        print 'year key not present'
        return None

def data_extractor(base_url):
    r = requests.get(base_url)
    html = BeautifulSoup(r.content)

    all_tables = html.findAll('table')
    data = all_tables[4] #table where profit-loss data contains
    years = []
    for year in data.tr.findAll('td'):
        if len(year.text)>3:
            years.append(year.text.replace("'", ""))
    info = {}
    for row in data:
        try:
            if row.td.text:
                info[row.td.text] = []
                for nums in row.findAll('td'):
                    try:
                        info[row.td.text].append(float(nums.text.replace(',', '')))
                    except ValueError:
                        pass
        except AttributeError:
            pass
    info['years'] = years
    for k in dict(info):
        if not info[k]:
            del info[k]
    return info
    #for k, v in info.iteritems():
    #    print k, v

def main():
    print "=" * 50
    print "Stock extractor"
    print "=" * 50
    base_url = raw_input("Give stock url: ")

    info = data_extractor(base_url)
    pretty_info = make_pretty(info)


if __name__ == '__main__':
    main()
