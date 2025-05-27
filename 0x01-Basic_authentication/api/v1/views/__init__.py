#!/usr/bin/env python3
""" Initializes Blueprint and loads routes """
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

# Fix: import User before calling its method
from models.user import User

User.load_from_file()

