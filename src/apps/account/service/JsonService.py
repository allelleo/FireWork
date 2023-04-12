class JsonServiceManager:
    @staticmethod
    def user_to_json(user, c=None, nested=False):
        skillss = {}
        count = 0
        for skill in user.skills.all():
            skillss = {
                **skillss,
                f"{count}": {
                    'id': skill.id,
                    'title': skill.title
                }
            }
            count += 1
        print(skillss)
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
                        'spec': user.profile.spec
                    },
                    'rating': {
                        'score': user.rating.score
                    },
                    'portfolio': {
                        'data': user.portfolio.title,
                        'spec': user.portfolio.spec
                    },
                    'skills': skillss,
                    'notify': notify,
                    'photo': user.photo

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
                        'spec': user.profile.spec
                    },
                    'rating': {
                        'score': user.rating.score
                    },
                    'portfolio': {
                        'data': user.portfolio.title
                    },
                    'skills': skillss,
                    'notify': notify,
                    'photo': user.photo
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
                'spec': user.profile.spec
            },
            'rating': {
                'score': user.rating.score
            },
            'portfolio': {
                'data': user.portfolio.title
            },
            'skills': skillss,
            'notify': notify,
            'photo': user.photo
        }
