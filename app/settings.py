# -*- coding: utf-8 -*-
import os
import logging

# Logging config
logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M',
    format='%(asctime)s - %(levelname)s: %(message)s',
)

# Project config
APP_PATH = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = '@\x1b\xb6\x1b]\x1c\x93\xc0\xc9QI\x88\xd2\xa6\xd7i\x9cD\x92W\x90\x87\xee0'
