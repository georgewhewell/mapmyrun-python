class Client(object):

    """docstring for Client."""
    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret

    def get_redirect(self):
        print('I\'m getting a redirect')
        return True
