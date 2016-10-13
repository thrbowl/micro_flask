# -*- coding: utf-8 -*-
from app.home import blueprint


@blueprint.route('/')
def index():
    return 'ok'
