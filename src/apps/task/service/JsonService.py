from apps.account.service.JsonService import JsonServiceManager as JM
class JsonServiceManager:
    @staticmethod
    def task_to_json(task,c=None):
        return {
            'title':task.title,
            'description': task.description,
            'price': task.price,
            'deadlines': task.deadlines,
            'place': task.place,
            'link': task.get_url(),
            'author': JM.user_to_json(task.from_customer)
        }