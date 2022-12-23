class Config():
    DEBUG=False

class developmentConfig(Config):
    DEBUG=True

class productionConfig(Config):
    DEBUG=False