from apps.account.models import User
from apps.account.service.AppService import AccountServiceManager
from core import errors
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chat, Message
from apps.task.models import Task


# Create your views here.
class StartChatAPIView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response()

        token = request.data.get('token', None)
        chat_to = request.data.get('chat_to', None)
        task = request.data.get('task', None)
        try:
            chat_from = AccountServiceManager.get_user_from_jwt(token)

        except errors.NullToken:
            response.data = {'error': 'Не все данные заполенены'}
            return response
        except errors.WrongToken:
            response.data = {'error': 'Токен не верный'}
            return response
        except errors.UserNotFound:
            response.data = {'error': 'Пользователь не найден'}
            return response

        if not chat_to:
            response.data = {'error': 'Не все данные заполенены'}
            return response

        if not User.objects.filter(id=chat_to).exists():
            response.data = {'error': 'Нет такого пользователя'}
            return response

        chat_to = User.objects.get(id=chat_to)

        chat = Chat(task=Task.objects.get(id=task))
        chat.save()
        chat.messages.create(text='Вас пригласили в чат', from_user=chat_from, to_user=chat_to, viewed=False)
        chat_from.chats.add(chat)
        chat_to.chats.add(chat)
