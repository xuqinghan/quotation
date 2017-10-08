import requests
import json
import arrow

commodity1 = {'name':'铁矿', 'code':'i'}
continualcontract1 = {'commodity_code':'i', 'month':9}
contract1 = {'commodity_code':'i','year':2014,  'month':9}


quotation1 = {'category':'futures',
              'contract':contract1,
              'quotation':{
                  'datetime':arrow.get('20140102', 'YYYYMMDD').format(),
                  'scale_time':'D',
                  'open':891,
                  'high':893,
                  'low':883,
                  'close':889,
                  'vol':2986,
                  'open_interest':30844,
                }
              }


def add_commodity(commodity1):
    url = 'http://127.0.0.1:5000/futures/commodity/{code}'.format(code=commodity1['code'])         
    r = requests.put(url, data=commodity1)
    print(r.text)

def add_continualcontract(continualcontract1):
    url = 'http://127.0.0.1:5000/futures/continual/{code}/{month}'.format(code=continualcontract1['commodity_code'],
    month=continualcontract1['month'],
    )         
    r = requests.put(url, data=continualcontract1)
    print(r.text)

def add_contract(contract1):
    url = 'http://127.0.0.1:5000/futures/contract/{code}/{year}/{month}'.format(code=contract1['commodity_code'],
    year=contract1['year'],
    month=contract1['month'],
    )         
    r = requests.put(url, data=contract1)
    print(r.text)

def add_quotation(quotation1):
    url = 'http://127.0.0.1:5000/futures/quotation'
          
    r = requests.put(url, data=quotation1)
    print(r.text)

if __name__ == '__main__':
    #添加一个期货品种
    add_commodity(commodity1)
    #添加1个连续合约
    add_continualcontract(continualcontract1)
    #添加1个合约
    add_contract(contract1)
    #添加1个行情点
    add_quotation(quotation1)
