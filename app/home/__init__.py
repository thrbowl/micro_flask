# -*- coding: utf-8 -*-
from flask import Blueprint

pkg_name = __name__.split('.')[-1]
blueprint = Blueprint(__name__, __name__, url_prefix='/%s' % pkg_name)
