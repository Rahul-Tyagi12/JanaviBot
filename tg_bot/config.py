from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID =  762834285 # my telegram ID
    OWNER_USERNAME = "tonyironstark"  # my telegram username
    API_KEY = "1290469600:AAFQnCOzgx5FeT8RljkZ6Zh8qFk5zVolq-M"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://nocegendkrobxq:cd5642fc790eaa1b7c328048b48d88d26a594ab2c9c6f08a5c18ca034ec7cc5f@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d64too2r1bkab7'  # sample db credentials
    MESSAGE_DUMP = '-1001210615572' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
