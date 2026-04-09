import pytest
from app.infrastructure.adapter import CurrencyAdapter
from app.application.services import CurrencyService
from app.domain.currency import CurrencyInfo

@pytest.fixture
def adapter():
    return CurrencyAdapter()

@pytest.fixture
def service(adapter):
    return CurrencyService(adapter)

def test_adapter_fetches_real_data(adapter):
    result = adapter.get_currency_info()

    assert isinstance(result, list)
    assert len(result) > 0

    codes = [c.char_code for c in result]
    assert "USD" in codes
    assert "EUR" in codes

def test_adapter_fetches_historical_data(adapter):
    result = adapter.get_currency_info(date="01/01/2024")

    assert len(result) > 0
    usd = next(c for c in result if c.char_code == "USD")
    assert usd.value > 0

def test_adapter_returns_currency_info_objects(adapter):
    result = adapter.get_currency_info()
    assert all(isinstance(item, CurrencyInfo) for item in result)

def test_adapter_all_values_positive(adapter):
    result = adapter.get_currency_info()
    assert all(item.value > 0 for item in result)

def test_service_returns_dict(service):
    result = service.get_currency_report()
    assert isinstance(result, dict)
    assert "USD" in result
    assert "EUR" in result

def test_service_filter_by_currency(service):
    result = service.get_currency_report(char_code="USD")
    assert len(result) == 1
    assert "USD" in result
    assert isinstance(result["USD"], float)

def test_service_historical_data(service):
    result = service.get_currency_report(date="2024-06-15")
    assert isinstance(result, dict)
    assert len(result) > 0

def test_service_info(service):
    info = service.get_service_info()
    assert info.service == "currency"
    assert info.version is not None
    assert info.author is not None
