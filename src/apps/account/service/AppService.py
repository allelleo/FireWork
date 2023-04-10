from apps.account.models import User
from core import errors
import jwt
import datetime
from core.settings import JWT_ENCODE_SECRET_KEY, TOKEN_LIFE_CYCLE_IN_MINUTES, JWT_DECODE_SECRET_KEY
class AccountServiceManager:
    @staticmethod
    def get_user_from_jwt(token):
        if not token:
            raise errors.NullToken

        try:
            payload = jwt.decode(token, JWT_DECODE_SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise errors.WrongToken

        user = User.objects.filter(id=payload['id']).first()
        if user:
            return user
        else:
            raise errors.UserNotFound