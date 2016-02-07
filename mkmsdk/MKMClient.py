from oauthlib.oauth1 import Client


class MKMClient(Client):
    """
    A personalized OAuth1 Client used for Widget Applications
    """

    def get_oauth_params(self, request):
        """
        A modified version of the original method get_oauth_params,
        this version appends the `oauth_token` parameter as an empty
        string to the parameters list if not found in it
        """

        parameters = super(MKMClient, self).get_oauth_params(request)

        oauthParamExist = False
        # Loop through the parameters to check if oauth_token is found
        for param in parameters:
            if 'oauth_token' in param:
                oauthParamExist = True
                break

        # We append the empty string oauth_token if it's not already there
        if not oauthParamExist:
            parameters.append(('oauth_token', ''))

        return parameters
