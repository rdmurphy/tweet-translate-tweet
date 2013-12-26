from twython import TwythonStreamer

from translate import Translate
from tweet import Tweet

import config


class TweetStream(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            translated_text = Translate.translate_text(data['text'].encode('utf-8'), config.from_lang, config.to_lang)
            Tweet.update(translated_text)


stream = TweetStream(
    config.twitter_consumer_key,
    config.twitter_consumer_secret,
    config.twitter_access_token,
    config.twitter_access_secret
)

stream.statuses.filter(follow=config.watch_account_id)
