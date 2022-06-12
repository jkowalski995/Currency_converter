import connect


def calculate(code, code2, amount):
    """
    This function calculate the amount of money in new currency.

    :param code: Unified code of currency that user has
    :param code2: Unified code of currency that user want to have
    :param amount: Amount of money that user want to exchange
    :return: Amount of new currency after change
    """

    bid = connect.ask_about_currency(code)[0]

    ask2 = connect.ask_about_currency(code2)[1]

    amount_pln = amount * bid
    amount_new_curr = round(amount_pln / ask2, 2)

    return amount_new_curr


def calculate_one_way(code, amount):
    """
    This function calculate the amount of money in new currency but the old currency is Polish Zloty (PLN)

    :param code: Unified code of currency that user want to have
    :param amount: Amount of money that user want to exchange
    :return: Amount of new currency after change
    """


    ask = connect.ask_about_currency(code)[1]
    print(ask)
    amount_new_curr = round(amount / ask, 2)

    return amount_new_curr
