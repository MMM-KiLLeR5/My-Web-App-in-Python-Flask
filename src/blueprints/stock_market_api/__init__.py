from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from schemas.schemas import StockMarketMin, StockMarketGB
from Market.HandleStockMarket import Handler
from Constants import StockMarketApprovalMessages, StockMarketErrorMessages


stock_market_api = Blueprint('market', __name__, url_prefix='/market')

@stock_market_api.route('/min_table', methods=['GET'])
@marshal_with(StockMarketMin(many=True))
def get_minutes_table():
    return Handler.get_minutes_market()


@stock_market_api.route('/gb_table', methods=['GET'])
@marshal_with(StockMarketGB(many=True))
def get_gb_table():
    return Handler.get_gb_market()

@stock_market_api.route('/sell_min/<string:username>', methods=['PUT'])
@use_kwargs(StockMarketMin)
def create_offer_min(username, **kwargs):
    try:
        Handler.create_min_offer(username, **kwargs)
    except ValueError:
        return {'error': StockMarketErrorMessages.NOT_ENOUGH_MINUTE}, 405
    return {'message': StockMarketApprovalMessages.MINUTE_OFFERED_SUCCESSFULLY}, 200



@stock_market_api.route('/sell_gb/<string:username>', methods=['PUT'])
@use_kwargs(StockMarketGB)
def create_offer_gb(username, **kwargs):
    try:
        Handler.create_gb_offer(username, **kwargs)
    except ValueError:
        return {'error': StockMarketErrorMessages.NOT_ENOUGH_GB}, 405
    return {'message': StockMarketApprovalMessages.GB_OFFERED_SUCCESSFULLY}, 200


@stock_market_api.route('/buy_gb/<string:username>&<int:id>', methods=['POST'])
def buy_gb(username, id):
    if Handler.buy_gb(username, id):
        return {'error': StockMarketErrorMessages.NOT_ENOUGH_MONEY}, 405
    return {'message': StockMarketApprovalMessages.GB_BOUGHT_SUCCESSFULLY}, 200



@stock_market_api.route('/buy_min/<string:username>&<int:id>', methods=['POST'])
def buy_min(username, id):
    if Handler.buy_minutes(username, id):
        return {'error': StockMarketErrorMessages.NOT_ENOUGH_MONEY}, 405
    return {'message': StockMarketApprovalMessages.MINUTE_BOUGHT_SUCCESSFULLY}, 200

