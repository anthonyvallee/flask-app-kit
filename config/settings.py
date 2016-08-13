from os import path

# --- Flask configuration ---
DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeyfordev'

# --- Application configuration ---
APP_NAME = '<%= appName %>'
APP_ROOT = path.join(path.dirname(path.abspath(__file__)), '..')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
