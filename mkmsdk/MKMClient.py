from oauthlib.oauth1 import Client


class MKMClient(Client):
    def get_oauth_params(self, request):
        params = super(MKMClient, self).get_oauth_params(request)

        oauthParamExist = False
        for tuple in params:
            if 'oauth_token' in tuple:
                oauthParamExist = True
                break

        if not oauthParamExist:
            params.append(('oauth_token', ''))

        return params
