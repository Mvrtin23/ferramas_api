from flask import Blueprint, jsonify
from api.services.user_service import get_all_users
from api.services.product_service import get_all_products
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from api.services import payment_service


bp = Blueprint('routes', __name__)

def register_routes(app):
    app.register_blueprint(bp)

@bp.route('/users', methods=['GET'])
def users():
    return jsonify(get_all_users())

@bp.route('/products', methods=['GET'])
def products():
    return jsonify(get_all_products())

router = APIRouter()

@router.post("/crear_pago")
async def crear_pago(request: Request):
    data = await request.json()
    amount = data["amount"]
    session_id = data["session_id"]
    buy_order = data["buy_order"]
    return_url = data["return_url"]

    response = payment_service.crear_transaccion(amount, session_id, buy_order, return_url)
    return response  

@router.post("/retorno_pago")
async def retorno_pago(request: Request):
    form = await request.form()
    token_ws = form.get("token_ws")

    result = payment_service.confirmar_transaccion(token_ws)
    return result  