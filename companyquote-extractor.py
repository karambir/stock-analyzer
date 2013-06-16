
import requests
from BeautifulSoup import BeautifulSoup

base_site = "http://moneycontrol.com"

def extract_quote(html):
    all_links = html.findAll('a', attrs={'class': 'bl_12'})

    companies = {}

    for link in all_links:
        if link.b:
            companies[link.b.text] = [link.get('href'),]

    for company in companies:
        data = companies[company]
        data.append(data[0][data[0].rfind('/')+1:])
        companies[company] = data

    return companies

def main():
    base_url = "http://www.moneycontrol.com/stocks/top-companies-in-india/market-capitalisation-bse.html"
    print "Company Quotes extractor"
    print '='*40
    global base_site
    r = requests.get(base_url)
    html = BeautifulSoup(r.content)
    company_types = {}
    l = html.find('div', attrs={'class': 'lftmenu'}).ul.findAll('a')
    number_of_companies = 0
    for item in l:
        print 'Getting: ', item.text,
        r = requests.get(base_site+item.get('href'))
        html = BeautifulSoup(r.content)
        companies = extract_quote(html)
        number_of_companies += len(companies)
        print ' ', len(companies)
        company_types[item.text] = companies
    print '\nTotal found: ', number_of_companies


if __name__ == '__main__':
    main()
