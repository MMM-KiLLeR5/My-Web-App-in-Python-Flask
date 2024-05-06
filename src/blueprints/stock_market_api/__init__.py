from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from src.schemas.schemas import StockMarketMin, StockMarketGB
from src.Market.HandleStockMarket import Handler

stock_market_api = Blueprint('market', __name__, url_prefix='/market')

@stock_market_api.route('/minutes_table', methods=['GET'])
@marshal_with(StockMarketMin(many=True))
def get_minutes_table():
    return Handler.get_gb_market()


@stock_market_api.route('/gb_table', methods=['GET'])
@marshal_with(StockMarketMin(many=True))
def get_gb_table():
    pass


@stock_market_api.route('/buy_gb/<string:username>&<int:id>', methods=['GET'])
def buy_gb(username, id):
    pass


@stock_market_api.route('/buy_min/<string:username>&<int:id>', methods=['GET'])
def buy_min(username, id):
    pass
