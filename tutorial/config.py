from environs import Env

env = Env()
env.read_env()


class Config:
    DEBUG = env.bool('DEBUG')
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')
