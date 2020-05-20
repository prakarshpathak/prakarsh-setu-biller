from .JWTManager import JWTManager


class Authenticator:
    def __init__(self):
        self.token_manager = JWTManager()

    def authenticated(self, token):
        if len(token) < 1:
            return False
        else:
            return self.token_manager.verify(token)