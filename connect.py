import requests


def ask_about_currency(code):
    """
    This function connects to the api handled by Polish National Bank (NBP) and ask about currency value.

    :param code: Unified code of currency that user want to have
    :return: bid and ask values of currency in Polish Zloty (PLN)
    """

    code = str(code).lower()
    url = "http://api.nbp.pl/api/exchangerates/rates/c/"+code+"/"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers).json()
    bid = response['rates'][0]['bid']
    ask = response['rates'][0]['ask']

    return bid, ask
