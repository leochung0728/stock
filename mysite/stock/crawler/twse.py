import urllib
import json
from datetime import timedelta
from bs4 import BeautifulSoup
from selenium import webdriver

from stock.models import Stock, Transaction
from mysite.utils import datetimeUtil

base_url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX'
url = ''
query_dict = {
    'date': '',
    'response': 'json',
    'type': 'ALL',
}

class spider_twse():
    date = ''

    def __init__(self, start_date='', end_date=''):
        self.start_date = datetimeUtil.str_parse_time(start_date)
        self.end_date = datetimeUtil.str_parse_time(end_date)
        self._check_date_parameter()
        self.error = 0

    def crawler(self):
        while self.start_date <= self.end_date and self.error <= 5:
            try:
                self.date = self.start_date
                self.crawl()
            except:
                self.error += 1
            finally:
                self.start_date += timedelta(1)


    def crawl(self):
        self.url = self.make_url()
        driver = webdriver.PhantomJS()
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        jsonResponse = json.loads(soup.text)
        datas = jsonResponse.get('data5')
        if isinstance(datas, list):
            for data in datas:
                stock, created = Stock.objects.get_or_create(code=data[0], defaults={'name': data[1]})
                sign = '-' if data[9].find('green') > 0 else ''
                Transaction.objects.update_or_create(code=stock, date=self.date, defaults={
                    'volume': self._transform_str_to_float(data[3].replace(',','')),
                    'final_price': self._transform_str_to_float(data[4].replace(',','')),
                    'opening_price': self._transform_str_to_float(data[5].replace(',','')),
                    'closing_price': self._transform_str_to_float(data[8].replace(',','')),
                    'highest_price': self._transform_str_to_float(data[6].replace(',','')),
                    'lowest_price': self._transform_str_to_float(data[7].replace(',','')),
                    'price_diff': self._transform_str_to_float(sign + data[10].replace(',','')),
                })
                print(stock.pk, self.date)

    def _check_date_parameter(self):
        self.start_date = self.end_date if self.start_date > self.end_date else self.start_date

    def make_url(self):
        query_dict['date'] = self.date.strftime('%Y%m%d')
        return "{0}?{1}".format(base_url, urllib.urlencode(query_dict))

    def _transform_str_to_float(self, valueStr):
        try:
            return float(valueStr)
        except (ValueError):
            return None