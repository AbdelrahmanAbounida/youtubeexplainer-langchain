

class Config:
    SECRET_KEY = '7c112dfe58c7733bb5132ef23218d349'
    DEBUG = True

class DevelopmentConfig(Config):
    SECRET_KEY = '7c112dfe58c7733bb5132ef23218d349'
    DEBUG = True

class TestingConfig(Config):
    SECRET_KEY = '7c112dfe58c7733bb5132ef23218d349'
    DEBUG = False

class DeploymentConfig(Config):
    SECRET_KEY = '7c112dfe58c7733bb5132ef23218d349'
    DEBUG = False


config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'deployment':DeploymentConfig,
    'default':DevelopmentConfig
}