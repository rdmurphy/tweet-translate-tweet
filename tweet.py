from twython import Twython, TwythonError

import config


class Tweet(object):
    def __init__(self):
        self.client = Twython(
            config.twitter_consumer_key,
            config.twitter_consumer_secret,
            config.twitter_access_token,
            config.twitter_access_secret
        )

    def update(self, text):
        try:
            self.client.update_status(status=text)
        except TwythonError, e:
            if e.error_code == 403:
                pass
