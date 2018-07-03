from configurer import config

# reddit app
USERNAME = config.get_configuration("username")
PASSWORD = config.get_configuration("password")
CLIENT_ID = config.get_configuration("client_id")
CLIENT_SECRET = config.get_configuration("client_secret")

# subreddit information
USER_AGENT = config.get_configuration("user_agent")
SUBREDDIT = config.get_configuration("subreddit_name")
