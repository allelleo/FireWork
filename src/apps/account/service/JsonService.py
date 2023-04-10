class JsonServiceManager:
    @staticmethod
    def user_to_json(user, c=None, nested=False):
        skills = {}
        count = 0
        for skill in user.skills.all():
            slills = {
                **skills,
                f"{count}": {
                    'title': skill.title
                }
            }
            count += 1
        notify = {}
        count = 0
        for n in user.notification.all():
            notify = {
                **notify,
                f"{count}": {
                    'title': n.title
                }
            }
        if c != None:
            return {
                f"{c}": {
                    'id': user.id,
                    'name': user.name,
                    'surname': user.surname,
                    'last_name': user.last_name,
                    'phone': user.phone,
                    'email': user.email,
                    'is_customer': user.is_customer,
                    'profile': {
                        "description": user.profile.description,
                    },
                    'rating': {
                        'score': user.rating.score
                    },
                    'portfolio': {
                        'data': user.portfolio.title
                    },
                    'skills': skills,
                    'notify': notify
                }
            }
        if nested == True:
            return {
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'surname': user.surname,
                    'last_name': user.last_name,
                    'phone': user.phone,
                    'email': user.email,
                    'is_customer': user.is_customer,
                    'profile': {
                        "description": user.profile.description,
                    },
                    'rating': {
                        'score': user.rating.score
                    },
                    'portfolio': {
                        'data': user.portfolio.title
                    },
                    'skills': skills,
                    'notify': notify
                }
            }

        return {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'last_name': user.last_name,
            'phone': user.phone,
            'email': user.email,
            'is_customer': user.is_customer,
            'profile': {
                "description": user.profile.description,
            },
            'rating': {
                'score': user.rating.score
            },
            'portfolio': {
                'data': user.portfolio.title
            },
            'skills': skills,
            'notify': notify
        }
