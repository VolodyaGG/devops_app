import pytest
from unittest.mock import MagicMock
from app.application.services import CurrencyService
from app.domain.currency import CurrencyInfo

@pytest.fixture
def mock_port():
    return MagicMock()

@pytest.fixture
def service(mock_port):
    return CurrencyService(mock_port)

def test_get_currency_report_full_list(service, mock_port):
    mock_port.get_currency_info.return_value = [
        CurrencyInfo(char_code="USD", value=75.0),
        CurrencyInfo(char_code="EUR", value=85.0),
        CurrencyInfo(char_code="GBP", value=100.0)
    ]

    result = service.get_currency_report()

    assert result == {"USD": 75.0, "EUR": 85.0, "GBP": 100.0}
    mock_port.get_currency_info.assert_called_once()

def test_get_currency_report_with_filter(service, mock_port):
    mock_port.get_currency_info.return_value = [
        CurrencyInfo(char_code="USD", value=75.0),
        CurrencyInfo(char_code="EUR", value=85.0)
    ]

    result = service.get_currency_report(char_code="eur")

    assert result == {"EUR": 85.0}
    assert "USD" not in result

def test_get_currency_report_not_found(service, mock_port):
    mock_port.get_currency_info.return_value = [
        CurrencyInfo(char_code="USD", value=75.0)
    ]

    result = service.get_currency_report(char_code="BITCOIN")

    assert "USD" in result
    assert "BITCOIN" not in result

def test_service_info_defaults(service):
    info = service.get_service_info()
    assert info.service == "currency"
    assert info.author == "v.laptev"