from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from jwt import decode, ExpiredSignatureError, PyJWTError
from jwt.algorithms import RSAAlgorithm

class Auth0JWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        try:
            header = decode(raw_token, verify=False)
            if 'kid' not in header:
                raise InvalidToken('Token has no kid')
            key = PUBLIC_KEY
            return decode(raw_token, key, algorithms=ALGORITHMS, audience=API_IDENTIFIER, issuer=f'https://{AUTH0_DOMAIN}/')
        except ExpiredSignatureError:
            raise InvalidToken('Token has expired')
        except PyJWTError as e:
            raise InvalidToken(str(e))