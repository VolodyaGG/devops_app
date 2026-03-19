from app.application.ports import CurrencyPort
from app.domain.info import ServiceInfo
from dotenv import load_dotenv
import os

class CurrencyService:
    def __init__(self, port: CurrencyPort):
        self.port = port

    def get_currency_report(self, date: str | None = None, char_code: str | None = None):
        currencies = self.port.get_currency_info(date)

        result = {}
        for currency in currencies:
            result[currency.char_code] = currency.value

        if char_code and char_code.upper() in result.keys():
            char_code = char_code.upper()
            return {char_code: result.get(char_code)}
        return result
    
    def get_service_info(self):
        load_dotenv()
        return ServiceInfo(
            version=os.getenv("VERSION") or "1.0.0",
            service="currency",
            author=os.getenv("AUTHOR") or "v.laptev"
        )

