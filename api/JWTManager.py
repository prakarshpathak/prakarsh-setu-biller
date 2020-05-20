import jwt
import datetime
import uuid


class JWTManager:
    def __init__(self):
        self.scheme_id = "8f47e41c-4684-4af1-b1b8-246c83112033"
        self.secret = "7c2e036c-908f-48ba-abe3-cd8745a6fa99"
        self.payload = {
            "aud": self.scheme_id,
            "iat": datetime.datetime.utcnow(),
            "jti": str(uuid.uuid1())
        }

    def issue(self):
        return jwt.encode(self.payload, self.secret, algorithm="HS256")

    def verify(self, token):
        try:
            # verified claim
            jwt.decode(token, self.secret, audience=self.scheme_id)
            verified = True
        except jwt.PyJWTError:
            verified = False

        return verified