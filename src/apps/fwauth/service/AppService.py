from apps.account.models import User, UserRating, UserProfile, UserPortfolio, UserSkills
from core import errors
import jwt
import datetime
from core.settings import JWT_ENCODE_SECRET_KEY, TOKEN_LIFE_CYCLE_IN_MINUTES


class AuthServiceManager:
    @staticmethod
    def create_user(name, surname, last_name, phone, email, is_customer, password):
        if not name:
            raise errors.NullValue
        if not surname:
            raise errors.NullValue
        if not email:
            raise errors.NullValue
        if not password:
            raise errors.NullValue
        if not phone:
            raise errors.NullValue
        if not is_customer and is_customer != False:
            raise errors.NullValue

        if User.objects.filter(email=email).exists():
            raise errors.UniqueEmail
        if User.objects.filter(phone=phone).exists():
            raise errors.UniquePhone

        profile = UserProfile()
        profile.save()

        rating = UserRating()
        rating.save()

        portfolio = UserPortfolio()
        portfolio.save()

        user = User(name=name, surname=surname, email=email, last_name=last_name, phone=phone)
        user.set_password(password)

        user.profile = profile
        user.rating = rating
        user.portfolio = portfolio

        user.save()

        return user

    @staticmethod
    def login(email, password):
        if not email:
            raise errors.NullValue
        if not password:
            raise errors.NullValue

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                raise errors.NotFoundUserByEmail
        else:
            raise errors.WrongPassword

    @staticmethod
    def generate_token(user_id):
        payload = {
            'id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_LIFE_CYCLE_IN_MINUTES),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload=payload, key=JWT_ENCODE_SECRET_KEY, algorithm='HS256')

        return token
