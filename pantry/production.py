import os
import dj_database_url

from .settings import *

ALLOWED_HOSTS = ["pantry-backend-prod.herokuapp.com"]
DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASES = {"default": dj_database_url.config(conn_max_age=600)}
