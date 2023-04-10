from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from core import errors
from .service.AppService import AuthServiceManager


# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):

        response = Response()

        name = request.data.get('name', None)
        surname = request.data.get('surname', None)
        last_name = request.data.get('last_name', None)
        phone = request.data.get('phone', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        is_customer = request.data.get('is_customer', None)


        try:
            r = AuthServiceManager.create_user(name, surname, last_name, phone, email, is_customer, password)
            response.data = {
                'status': 'success',
                'id': r.id
            }
            return response
        except errors.NullValue:
            response.data = {'error': 'Не все данные заполенены'}
            return response
        except errors.UniqueEmail:
            response.data = {'error': 'Этот email уже используется'}
            return response

        except errors.UniquePhone:
            response.data = {'error': 'Этот телефон уже используется'}
            return response


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):

        response = Response()

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        try:
            r = AuthServiceManager.login(email, password)
            token = AuthServiceManager.generate_token(r.id)
            response.data = {'token': token}
            return response
        except errors.NullValue:
            response.data = {'error': 'Не все данные заполенены'}
            return response
        except errors.NotFoundUserByEmail:
            response.data = {'error': 'Нет пользователя с такой почтой'}
            return response
        except errors.WrongPassword:
            response.data = {'error': 'Неверный пароль'}
            return response
