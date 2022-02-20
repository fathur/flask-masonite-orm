"""
Docstring
"""
import os

from flask import Flask, Blueprint
from flask_restful import Resource, Api

from app.resources import ApplicationListResource, ApplicationItemResource
from app.routes.application_flow import routes as application_flow_routes
from app.routes.auth import routes as auth_routes


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    application_flow_blueprint = Blueprint('application_flow', __name__)
    auth_blueprint = Blueprint('auth', __name__)
    application_flow = Api(application_flow_blueprint)
    auth = Api(auth_blueprint)

    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    #
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    application_flow_routes(application_flow)
    auth_routes(auth)

    app.register_blueprint(application_flow_blueprint, url_prefix='/v1')
    app.register_blueprint(auth_blueprint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
