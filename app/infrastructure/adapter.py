import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from app.application.ports import CurrencyPort
from app.domain.currency import CurrencyInfo

class CurrencyAdapter(CurrencyPort):
    def get_currency_info(self, date: str | None = None) -> list[CurrencyInfo]:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        cdr_date = ""
        if date:
            try:
                dt_obj = datetime.strptime(date, "%Y-%m-%d")
                cdr_date = dt_obj.strftime("%d.%m.%Y")
            except ValueError:
                cdr_date = ""
        response = requests.get(url, params={'date_req': cdr_date})
        response.raise_for_status()
        response = ET.fromstring(response.content)

        currencies = []
        for element in response.findall('Valute'):
            char_code = element.find('CharCode').text
            val = float(element.find('Value').text.replace(",", "."))
            currencies.append(CurrencyInfo(char_code=char_code, value=val))
        return currencies
