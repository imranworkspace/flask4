from app.extentions import db,migrate
from flask import Flask
import os 
from app.routers.labor_router import labor_bp
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
    print(app.config.get('SQLALCHEMY_DATABASE_URI'))
    db.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(
        labor_bp,
        url_prefix='/api'
    )

    return app 