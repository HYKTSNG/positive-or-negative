import os
from dotenv import load_dotenv
import oauth2 as oauth


# --------------------------------------------------------------------
def define_client_proc():
    dotenv_path = '../.env'
    load_dotenv(dotenv_path)
    API_key = os.environ.get('API_key')
    API_secret_key = os.environ.get('API_secret_key')
    Access_token = os.environ.get('Access_token')
    Access_secret_token = os.environ.get('Access_secret_token')
    #
    consumer = oauth.Consumer(key=API_key, secret=API_secret_key)
    access_token = oauth.Token(key=Access_token, secret=Access_secret_token)
    client = oauth.Client(consumer, access_token)
    #
    return client
