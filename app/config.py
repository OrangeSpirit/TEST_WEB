import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'web_user')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'web_password')
    HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    PORT = os.environ.get('POSTGRES_PORT', '5432')
    DB = os.environ.get('POSTGRES_DB', 'web_db')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'euiryweur802480294803rjsdjfhnv'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
