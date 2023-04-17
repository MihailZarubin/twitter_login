import json


class UsersRepository:

    @staticmethod
    def get_all_users():
        with open('../users.json', 'r') as f:
            data = json.load(f)

        return data
