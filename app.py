from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource,Api
from flask_jwt import JWT
from db_exts import db,migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db.init_app(app)
migrate.init_app(app,db)

api = Api(app)
from resources.user import UserRegister
from resources.item import ItemListResource,ItemResource
from resources.store import Store,StoreList
from security import authenticate,identity
jwt = JWT(app,authenticate,identity)


api.add_resource(ItemResource,"/item/<string:name>")
api.add_resource(ItemListResource,"/items")
api.add_resource(UserRegister,"/register")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")


if __name__ == '__main__':
    app.run(port=5000,debug=True)
    