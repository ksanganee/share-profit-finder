import requests
import os
import json


def get_exchange_rate():
    rate_url = "https://api.exchangeratesapi.io/latest?base=GBP"
    rate_r = requests.get(rate_url)
    rate = json.loads(rate_r.text)["rates"]["USD"]
    return(rate)

def get_profit():
    lvs_spent = os.getenv("LVS_SPENT")
    lvs_stocks = os.getenv("LVS_STOCKS")
    lvs_url = "https://financialmodelingprep.com/api/v3/stock/real-time-price/LVS?apikey=" + str(os.getenv("API_KEY"))
    lvs_r = requests.get(lvs_url)
    lvs_price = json.loads(lvs_r.text)["price"]
    lvs_value = lvs_stocks * lvs_price
    lvs_profit = lvs_value - lvs_spent

    mgm_spent = os.getenv("MGM_SPENT")
    mgm_stocks = os.getenv("MGM_STOCKS")
    mgm_url = "https://financialmodelingprep.com/api/v3/stock/real-time-price/MGM?apikey=" + str(os.getenv("API_KEY"))
    mgm_r = requests.get(mgm_url)
    mgm_price = json.loads(mgm_r.text)["price"]
    mgm_value = mgm_stocks * mgm_price
    mgm_profit = mgm_value - mgm_spent

    net_profit_USD = mgm_profit + lvs_profit
    net_profit_GBP = net_profit_USD / get_exchange_rate()
    net_profit_GBP = round(net_profit_GBP, 2)

    pounds_pence = str(net_profit_GBP).split('.')
    return pounds_pence[0] + " pounds and " + pounds_pence[1] + " pence"

print(get_profit())
