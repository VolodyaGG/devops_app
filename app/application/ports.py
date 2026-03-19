from abc import ABC, abstractmethod
from app.domain.currency import CurrencyInfo

class CurrencyPort(ABC):
    @abstractmethod
    def get_currency_info(self, date: str | None = None) -> list[CurrencyInfo]:
        pass