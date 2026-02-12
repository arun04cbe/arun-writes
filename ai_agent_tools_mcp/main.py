from fastmcp import FastMCP
import requests

my_custom_app = FastMCP(name="exchange-rate-finder", port=8005)
EXCHANGE_API_BAS_URL = "https://api.exchangerate-api.com/v4/latest"


@my_custom_app.tool
def get_exchange_rates(country_code: str):
    """
    Get the exchange rate for the give country_code

    args:
    country_code:str - Country Code for which the exchange rate needs to be determined

    returns:
    dict - A dictionary containing the value for 1 currency in the given country code with other different countries.
    """
    URL = f"{EXCHANGE_API_BAS_URL}/{country_code}"
    result = requests.get(url=URL)
    if result and result.status_code == 200:
        return result.json()
    return "Error Occurred!"


if __name__ == "__main__":
    my_custom_app.run(transport="sse")
