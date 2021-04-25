from storage.storage import Storage


class UserService:
    __slots__ = ['storage']

    def __init__(self, storage: Storage):
        self.storage = storage

    async def create_user(self):
        pass