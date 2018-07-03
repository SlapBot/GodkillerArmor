from configurer import config

# reddit app
username = config.get_configuration("username")
password = config.get_configuration("password")

# subreddit information
user_agent = config.get_configuration("user_agent")
subreddit = config.get_configuration("subreddit_name")
