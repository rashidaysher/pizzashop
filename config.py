class Config:
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pjnr:peter1010@localhost/pizza1'


config_options = {
    'development': DevConfig
}
