import requests
from lxml import etree

import config


class Translate(object):
    auth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    translate_url = 'http://api.microsofttranslator.com/V2/Http.svc/Translate'

    def get_access_token(self):
        req = requests.post(self.auth_url, data={
            'grant_type': 'client_credentials',
            'scope': 'http://api.microsofttranslator.com',
            'client_id': config.ms_client_id,
            'client_secret': config.ms_client_secret,
        })

        return req.json()['access_token']


    def translate_text(self, text, from_lang, to_lang):
        payload = {
            'text': text,
            'from': from_lang,
            'to': to_lang,
        }

        headers = {
            'Authorization': 'bearer {0}'.format(self.get_access_token())
        }

        req = requests.get(self.translate_url, params=payload, headers=headers)

        return etree.XML(req.text).text
