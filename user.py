from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        user = UserDatabase.get_user_by_id(user_id)
        if user:
            return User(user_id, user['username'], user['password'])
        return None
