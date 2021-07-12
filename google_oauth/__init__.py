# python standard libraries
from pathlib import Path
import logging.config

# third party libraries
from flask import Flask
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import yaml

# logging
path_to_config_file = Path(__file__).parent / "config/config.yaml"
logging.config.fileConfig(path_to_config_file, disable_existing_loggers=False)

# create logger
logger = logging.getLogger("flaskapp")

with open(rf"{path_to_config_file}") as cfgfile:
    logger.info(f"loading configuration from config {path_to_config_file}")
    config = yaml.load(cfgfile, Loader=yaml.FullLoader)
    flask_app_conf = config["FLASK_APP_CONFIGURATION"]
    google_conf = config["GOOGLE_CONFIG"]
    db_conf = config["DB_CONFIG"]
    logger.info(f"=========Flask app Config========\n")
    logger.debug(f"{flask_app_conf}")
    logger.info(f"=========Google Config========\n")
    logger.debug(f"{google_conf}")
    logger.info(f"=========db  Config========\n")
    logger.debug(f"{db_conf}")

# flask app config
secret_key = flask_app_conf["secret_key"]
port = flask_app_conf["port"]
debug = flask_app_conf["debug"]
host = flask_app_conf["host"]

# google config
google_discovery_url = google_conf["google_discovery_url"]
google_redirect_uri = google_conf["google_redirect_uri"]
google_client_id = google_conf["google_client_id"]
google_client_secret = google_conf["google_client_secret"]

# db conf
SQLALCHEMY_DATABASE_URI = db_conf["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = db_conf["SQLALCHEMY_TRACK_MODIFICATIONS"]

# create flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

# add extensions to our app
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# user session management
login_manager = LoginManager()
login_manager.init_app(app)

# Oauth2 client setup
client = WebApplicationClient(google_client_id)
from google_oauth import routes






























