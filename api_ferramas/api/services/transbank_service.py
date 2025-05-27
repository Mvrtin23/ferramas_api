from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.integration_type import IntegrationType


Transaction.commerce_code = '597055555532'  
Transaction.api_key = '597055555532'        
Transaction.integration_type = IntegrationType.TEST

def iniciar_pago(amount, session_id, buy_order, return_url):
    response = Transaction.create(buy_order, session_id, amount, return_url)
    return response

def confirmar_pago(token):
    response = Transaction.commit(token)
    return response
