from twython import TwythonStreamer

from translate import Translate
from tweet import Tweet

import config

translator = Translate()
tweeter = Tweet()

class TweetStream(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data and not 'retweeted_status' in data and not data['in_reply_to_screen_name'] and data['user']['id_str'] == config.watch_account_id:
            translated_text = translator.translate_text(data['text'].encode('utf-8'), config.from_lang, config.to_lang)
            tweeter.update(translated_text)

stream = TweetStream(
    config.twitter_consumer_key,
    config.twitter_consumer_secret,
    config.twitter_access_token,
    config.twitter_access_secret
)

print('Beginning streaming.')
stream.statuses.filter(follow=config.watch_account_id)
