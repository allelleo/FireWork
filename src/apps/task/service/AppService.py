from apps.task.models import Task, TaskCategory
from core import errors
class TaskServiceManager:
    @staticmethod
    def create_task(user, title, description, price, deadlines, place, category, photo):
        if not title:
            raise errors.NullValue

        if not description:
            raise errors.NullValue

        if not price:
            raise errors.NullValue

        if not deadlines:
            raise errors.NullValue

        if not place:
            raise errors.NullValue


        task = Task(title=title, description=description, price=price, deadlines=deadlines, place=place)
        task.from_customer = user
        if photo:
            task.photo = photo
        if category:
            for cat in category:
                if TaskCategory.objects.filter(id=cat).exists():
                    task.category.add(TaskCategory.objects.get(id=cat))

        task.save()
        return task
