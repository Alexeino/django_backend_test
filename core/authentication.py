from rest_framework import exceptions
import jwt
from datetime import datetime,timedelta

def create_access_token(id):
    return jwt.encode({
        'user_id':id,
        'exp': datetime.utcnow() + timedelta(seconds=350),
        'iat': datetime.now()
    },'access_secret',algorithm='HS256')


def create_refresh_token(id):
    return jwt.encode({
        'user_id':id,
        'exp': datetime.utcnow() + timedelta(days=7),
        'iat': datetime.now()
    },'refresh_secret',algorithm='HS256')
    
def decode_access_token(token):
    try:
        payload = jwt.decode(token,'access_secret','HS256')
        print("PAYLOAD User id",payload.user_id)
        return payload.user_id
    except Exception as e:
        print(e)
        raise exceptions.AuthenticationFailed("Unauthenticated!")

    