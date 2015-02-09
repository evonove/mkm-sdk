from requests_oauthlib import OAuth1

class BuggedOAuth1(OAuth1):
    def __call__(self, r):

        return