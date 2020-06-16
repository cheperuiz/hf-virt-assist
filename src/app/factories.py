from importlib import import_module

from flask import Flask
from flask_restx import Api


def make_flask():
    flask_app = Flask(__name__)
    flask_app.config["SECRET_KEY"] = "SUPER-SECRET-KEY-HERE"
    flask_app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
    api = make_api()
    api.init_app(flask_app)
    return flask_app


RESOURCES = ["quotes"]


def make_api():
    api = Api(prefix="/hf", title="HF Virtual Assistant", version="1", catch_all_404s=True)

    for module_name in RESOURCES:
        module = import_module("." + module_name, "app.resources")
        namespace = getattr(module, "ns")
        api.add_namespace(namespace)
        return api
