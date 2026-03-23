import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SECRET_KEY= os.getenv('SECRET_KEY', 'dev-secret-key')
    AUTHGEAR_CLIENT_SECRET = os.getenv('AUTHGEAR_CLIENT_SECRET')
    AUTHGEAR_CLIENT_ID = os.getenv('AUTHGEAR_CLIENT_ID')
    AUTHGEAR_ISSUER = os.getenv('AUTHGEAR_ISSUER')
    AUTHGEAR_REDIRECT_URI = os.getenv('AUTHGEAR_REDIRECT_URI')
