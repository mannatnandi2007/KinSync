import os

class Config:
    
    SECRET_KEY = "kinsync_secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root123@localhost/kinsync_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False