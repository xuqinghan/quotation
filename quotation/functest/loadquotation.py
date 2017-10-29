import pandas as pd

COLUMNS_USED = ['合约','日期','开盘价','最高价','最低价','收盘价','结算价','成交量','持仓量']

def load_futures(f_name):
    '''读期货行情'''
    df = pd.read_csv(f_name, engine='python')
    return df[COLUMNS_USED]

def find_contract_by_name(name_contract, df):
    '''根据合约名称过滤'''
    return df[df['合约']==name_contract]

def contract_to_json(df_contract1):
    return df_contract1.to_json(orient='records',force_ascii=False)

if __name__ == '__main__':
    #添加一个期货品种
    f_name = 'D:\\project\\dev\\quotation\\quotation\\functest/2014i/铁矿石.csv'
    df = load_futures(f_name)
    name_contract = 'i1409'
    df_contract1 = find_contract_by_name(name_contract, df)
    #取前10行
    df_contract1 = df_contract1.head(n=10)
    contract_json = contract_to_json(df_contract1)
    print(contract_json)
