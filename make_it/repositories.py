class UserRepository:
    def add(self, user):
        raise NotImplementedError()

    def get(self, user_id):
        raise NotImplementedError()

    def update(self, user_id, update_data):
        raise NotImplementedError()

    def delete(self, user_id):
        raise NotImplementedError()
