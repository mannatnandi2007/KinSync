from flask import Flask
from config import Config
from extensions import db
from routes.auth_routes import auth


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth)

    @app.route("/")
    def home():
        return "KinSync Backend Running 🚀"
    
    @app.route("/dashboard")
    def dashboard():
        return "Welcome to KinSync Dashboard 🎉"

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)