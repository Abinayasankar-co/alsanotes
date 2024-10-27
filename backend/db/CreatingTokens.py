import jwt
import datetime
import secrets
from tzlocal import  get_localzone


def create_Token(payload, algorithm="HS256"):
    # Add expiration time if not included in the payload\
    secret = secrets.token_urlsafe(32) 

    tz = get_localzone()

    if "exp" not in payload:
        payload["exp"] = datetime.datetime.now(tz) + datetime.timedelta(hours=1)
    
    # Generate the JWT token
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

# Example usage
"""
payload = {
    "user_id": 123,
    "username": "example_user"
}
token = create_Token(payload)
print("Generated JWT:", token)

"""
