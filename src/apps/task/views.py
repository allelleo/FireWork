import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from core import errors
from apps.account.service.AppService import AccountServiceManager
from .service.AppService import TaskServiceManager
from .models import Task, TaskCategory, TaskAnswer
from .service.JsonService import JsonServiceManager

# Create your views here.
class CreateTaskAPIView(APIView):
    def post(self, request, *args, **kwargs):

        response = Response()
        token = request.data.get('token', None)
        try:
            user = AccountServiceManager.get_user_from_jwt(token)
        except errors.NullToken:
            response.data = {'error': 'Нет токена'}
            return response
        except jwt.ExpiredSignatureError:
            response.data = {'error': 'Токен не правильный'}
            return response
        except errors.UserNotFound:
            response.data = {'error': 'Пользователь не найден'}
            return response

        if not user.is_customer:
            response.data = {'error': 'Вы не заказчик, а исполнитель'}
            return response
        title = request.data.get('title', None)
        description = request.data.get('description', None)
        price = request.data.get('price', None)
        deadlines = request.data.get('deadlines', None)
        place = request.data.get('place', None)
        category = request.data.get('category', None)
        photo = request.data.get('photo', None)

        try:
            task = TaskServiceManager.create_task(user, title, description, price, deadlines, place, category, photo)
            response.data = {
                'status': 'success',
                'task': str(task.id)
            }
            return response

        except errors.NullValue:
            response.data = {'error': 'Не все данные заполенены'}
            return response


class ReadTaskAPIView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response()
        task_id = request.data.get('task_id', None)
        if not task_id:
            response.data = {
                'error': "id  нет"
            }
            return response

        if Task.objects.filter(id=task_id).exists():
            task = Task.objects.get(id=task_id)
            response.data = JsonServiceManager.task_to_json(task)
            return response
        response.data = {
            'error': "Задания с таким id  нет"
        }
        return response

class CreateTaskAnswer(APIView):
    def post(self, request, *args):
        response = Response()
        token = request.data.get('token', None)
        try:
            user = AccountServiceManager.get_user_from_jwt(token)
        except errors.NullToken:
            response.data = {'error': 'Нет токена'}
            return response
        except jwt.ExpiredSignatureError:
            response.data = {'error': 'Токен не правильный'}
            return response
        except errors.UserNotFound:
            response.data = {'error': 'Пользователь не найден'}
            return response

        task_id = request.data.get('task_id', None)
        comment = request.data.get('comment', None)
        if not task_id:
            response.data = {
                'error': "id  нет"
            }
            return response

        task = Task.objects.get(id=task_id)
        t = TaskAnswer(comment=comment, from_user=user,to_task=task)
        t.save()
        response.data = {
            'status': 'ok'
        }
        return response