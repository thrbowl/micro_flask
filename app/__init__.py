# -*- coding: utf-8 -*-
import logging

from flask import Flask
from flask_script import Manager as ScriptManager

from app import settings
from app.utils.funcational import get_reg_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(settings)
try:
    app.config.from_pyfile('settings.py')
except:
    pass

logging.debug('Initialize script manager')
script_manager = ScriptManager(app)

logging.debug('Register blueprints')
for bl in get_reg_blueprint(app.config['APP_PATH']):
    app.register_blueprint(blueprint=bl)
