from blueprints.admin_api.api import adm

from blueprints.stock_market_api.api import stock_market_api

from blueprints.user_api.api import user

from App import app, docs
from Tools.DocsRegister import docs_register

from Constants.Constant import Config

docs_register(app, docs, adm, '/api')
docs_register(app, docs, user, '/user')
docs_register(app, docs, stock_market_api, '/market')

if __name__ == "__main__":
    app.run(debug=True, host=Config.KNOWN_HOST, port=Config.PORT)

