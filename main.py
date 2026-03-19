import fastapi, uvicorn, os
from dotenv import load_dotenv
import app.infrastructure.adapter as CurrencyAdapter
import app.application.services as CurrencyService

load_dotenv()
app = fastapi.FastAPI()

def get_currency_service():
    adapter = CurrencyAdapter.CurrencyAdapter()
    service = CurrencyService.CurrencyService(adapter)
    return service

@app.get("/info")
def info():
    return get_currency_service().get_service_info()


@app.get("/info/currency")
def currency(date: str | None = None, currency: str | None = None):
    data = get_currency_service().get_currency_report(date, currency)
    return {
        "data": data,
        "service": "currency"
    }


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)