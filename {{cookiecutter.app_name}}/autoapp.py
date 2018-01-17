# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.public.forms import LoginForm
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)


@app.context_processor
def global_context_processor():
    return dict(navbar_login_form=LoginForm())
