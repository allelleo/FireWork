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

        if not (Chat.objects.filter(user1=chat_from).exists() and Chat.objects.filter(
                user2=chat_to).exists() and Chat.objects.filter(task=Task.objects.get(id=task)).exists()):
            chat = Chat(task=Task.objects.get(id=task))
            chat.user1 = chat_from
            chat.user2 = chat_to
            chat.save()
            chat.messages.create(text='Вас пригласили в чат', from_user=chat_from, to_user=chat_to, viewed=False)
            response.data = {'success': True}
            return response

        response.data = {'error': 'такой чат уже существует'}
        return response


class GetChatsForCurrentUserAPIView(APIView):
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

        user_chats = {}
        c = 0
        chats = list(Chat.objects.all().filter(user1=user)) + list(Chat.objects.all().filter(user2=user))
        for chat in chats:
            if chat.user1 != user:
                name = chat.user1.get_full_name()
            else:
                name = chat.user1.get_full_name()
            last = list(chat.messages.all())[-1]
            if last.from_user == user:
                last_message = "Вы:" + str(last.text)
            else:
                last_message = last.get_full_name() + str(last.text)
            user_chats = {
                **user_chats,
                **{
                    f"{c}": {
                        'chat_name': name,
                        'last_message': last_message,
                        'time': str(last.time),
                        'viewed': last.viewed,
                        'id': chat.id
                    }
                }
            }
            c += 1

        response.data = user_chats
        return response


class GetMessagesFromChatAPIView(APIView):
    def post(self, request):
        response = Response()
        chat_id = request.data.get('chat_id', None)
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

        if Chat.objects.filter(id=chat_id).exists():
            chat = Chat.objects.get(id=chat_id)
            msgs = {}
            c = 0
            for msg in chat.messages.all():
                if msg.from_user == user:
                    msgs = {
                        **msgs,
                        **{
                            f'{c}': {
                                'from': 'me',
                                'text': msg.text,
                                'time': str(msg.time),
                                'viewed': msg.viewed
                            }
                        }

                    }
                else:
                    msgs = {
                        **msgs,
                        **{
                            f'{c}': {
                                'from': msg.from_user.get_full_name(),
                                'text': msg.text,
                                'time': str(msg.time),
                                'viewed': msg.viewed
                            }
                        }

                    }
            c += 1

            response.data = msgs
            return response

class CreateMessage(APIView):
    def post(self, request):
        chat_id = request.data.get('chat_id')
        msg = request.data.get('msg')
        token = request.data.get('token', None)
        response = Response()
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

        chat = Chat.objects.get(id=chat_id)
        if chat.user1 != user:
            user2 = chat.user1
        else:
            user2 = chat.user2

        chat.messages.create(text=msg, from_user=user, to_user=user2)
        response.data = {'status': 'ok'}
        return response
