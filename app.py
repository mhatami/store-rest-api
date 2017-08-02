from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.store import Store, StoreList
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key='jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Store, '/store/<string:name>') #http://127.0.0.1:5000/itemt/<name>
api.add_resource(StoreList, '/stores') #http://127.0.0.1:5000/itemt/<name>

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/itemt/<name>
api.add_resource(ItemList, '/items') #http://127.0.0.1:5000/itemt/<name>
api.add_resource(UserRegister, '/register') #http://127.0.0.1:5000/itemt/<name>

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
