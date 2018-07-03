from settings import *
from praw import Reddit


class Savenger:
    def __init__(self):
        self.Reddit = Reddit
        self.reddit = object

    def authenticate(self, username, password, client_id, client_secret, user_agent):
        print("Authenticating...")
        try:
            self.reddit = self.Reddit(user_agent=user_agent, client_id=client_id,
                                      client_secret=client_secret, username=username,
                                      password=password)
            username = reddit.user.me()
            print(f"Authenticated as {username}")
            return self.reddit
        except Exception as e:
            print(e)
            exit()


if __name__ == '__main__':
    savenger = Savenger()
    reddit = savenger.authenticate(USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, USER_AGENT)
