from settings import *
from savenger import Savenger


savenger = Savenger()
savenger.authenticate(USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, USER_AGENT)

savenger.save(SUBREDDIT)
