from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.integration_type import IntegrationType
from transbank.webpay.webpay_plus.configuration import Configuration


Configuration.for_testing_webpay_plus()

def crear_transaccion(amount, session_id, buy_order, return_url):
    response = Transaction.create(
        buy_order=buy_order,
        session_id=session_id,
        amount=amount,
        return_url=return_url
    )
    return response

def confirmar_transaccion(token_ws):
    response = Transaction.commit(token_ws)
    return response

