import requests
import json


commodity1 = {'name':'铁矿', 'code':'i'}
continualcontract1 = {'commodity_code':'i','month':9}
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


if __name__ == '__main__':
    #添加一个期货品种
    add_commodity(commodity1)
    #添加1个合约
    add_continualcontract(continualcontract1)
