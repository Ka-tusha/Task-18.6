import requests
import json
from config import keys
class ConvertionExeption(Exception):
    pass

class CryptoConverter:
 @staticmethod
 def get_price(qoute: str, base: str, amount: str):
     if qoute == base:
         raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

     try:
         quote_ticker = keys[qoute]
     except KeyError:
         raise ConvertionExeption(f'Не удалось обработать валюту {qoute}')

     try:
         base_ticker = keys[base]

     except KeyError:
         raise ConvertionExeption(f'Не удалось обработать валюту {base}')

     try:
         amount = float(amount)
     except ValueError:
         raise ConvertionExeption(f'Не удалось обработать количество {amount}')

     r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}').json()

     return r[base_ticker]

