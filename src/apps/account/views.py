from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .service.AppService import AccountServiceManager
from core import errors
# Create your views here.

class EndpointView(APIView):
    def post(self, request, *args, **kwargs):

        response = Response()

        token = request.data.get('token', None)

        try:
            res = AccountServiceManager.get_user_from_jwt(token)
            response.data = {
                'username': res.username,
                'email': res.email,
            }
            return response
        except errors.NullToken:
            response.data = {'error': 'Не все данные заполенены'}
            return response
        except errors.WrongToken:
            response.data = {'error': 'Токен не верный'}
            return response
        except errors.UserNotFound:
            response.data = {'error': 'Пользователь не найден'}
            return response