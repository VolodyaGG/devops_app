import defusedxml.ElementTree as ET
from datetime import datetime
import requests
from app.application.ports import CurrencyPort
from app.domain.currency import CurrencyInfo


class CurrencyAdapter(CurrencyPort):
    def get_currency_info(self, date: str | None = None) -> list[CurrencyInfo]:
        url = "https://www.cbr.ru/scripts/XML_daily.asp"
        params = {}
        if date:
            try:
                dt_obj = datetime.strptime(date, "%Y-%m-%d")
                params["date_req"] = dt_obj.strftime("%d.%m.%Y")
            except ValueError:
                pass

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        currencies = []
        for element in root.findall("Valute"):
            char_code = element.find("CharCode").text
            val = float(element.find("Value").text.replace(",", "."))
            currencies.append(CurrencyInfo(char_code=char_code, value=val))

        return currencies