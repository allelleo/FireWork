from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .service.AppService import AccountServiceManager
from core import errors
from .service.JsonService import JsonServiceManager
from .models import UserSkills, User


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

class GetCurrentUserData(APIView):
    def post(self, request, *args, **kwargs):

        response = Response()

        token = request.data.get('token', None)

        try:
            res = AccountServiceManager.get_user_from_jwt(token)
            response.data = JsonServiceManager.user_to_json(res)
            print(response.data)
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

class ChangeUserPhoto(APIView):
    def post(self, request, *args):
        print(request.FILES['filename'].name)
        response = Response()
        response.data = {
            'pifor?': True
        }
        return response

class AddSkill(APIView):
    def post(self, request, *args):
        response = Response()

        token = request.data.get('token', None)

        try:
            user = AccountServiceManager.get_user_from_jwt(token)

        except errors.NullToken:
            response.data = {'error': 'Не все данные заполенены'}
            return response
        except errors.WrongToken:
            response.data = {'error': 'Токен не верный'}
            return response
        except errors.UserNotFound:
            response.data = {'error': 'Пользователь не найден'}
            return response

        skill_id = request.data.get('skill', None)
        if not skill_id:
            response.data = {'error': 'Пустой skill_id'}
            return response

        skill = UserSkills.objects.get(id=skill_id)
        user.skills.add(skill)
        response.data = {'skill': skill.id}
        return response

class AllSkills(APIView):
    def get(self, request):
        skills = {}
        c = 0
        for skill in UserSkills.objects.all():
            skills = {
                **skills,
                **{
                    f'{c}': {
                        'id': skill.id,
                        'title': skill.title
                    }
                }
            }
            c += 1
        response = Response()
        response.data = skills
        return response

class CreateFeedBack(APIView):
    def post(self, request):
        response = Response()

        token = request.data.get('token', None)

        try:
            user = AccountServiceManager.get_user_from_jwt(token)

        except errors.NullToken:
            response.data = {'error': 'Не все данные заполенены'}
            return response
        except errors.WrongToken:
            response.data = {'error': 'Токен не верный'}
            return response
        except errors.UserNotFound:
            response.data = {'error': 'Пользователь не найден'}
            return response

        work_title = request.data.get('work_title', None)
        feedback = request.data.get('feedback', None)
        stars = request.data.get('stars', None)
        to_user = request.data.get('to_user', None)
        to = User.objects.get(id=to_user)
        to.feedbacks.create(work_title=work_title, feedback=feedback, stars=stars)

class GetCustomers(APIView):
    def get(self, request):
        c = User.objects.filter(is_customer=True)
        users = {}
        count = 0
        for usr in c:
            users = {
                **users,
                **{
                    f"{count}": JsonServiceManager.user_to_json(usr)
                }
            }
        return users

class GetWorkers(APIView):
    def get(self, request):
        c = User.objects.filter(is_customer=False)
        users = {}
        count = 0
        for usr in c:
            users = {
                **users,
                **{
                    f"{count}": JsonServiceManager.user_to_json(usr)
                }
            }
        return users