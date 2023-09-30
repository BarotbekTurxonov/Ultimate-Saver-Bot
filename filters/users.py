from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from loader import db


class IsUser(BoundFilter):
    async def check(self, message: types.Message):
        user_id =message.from_user.id
        user = db.is_user(user_id=user_id)
        if user:
            return True
        else:
            return False


class IsGuest(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id
        user = db.is_user(user_id=user_id)
        if user:
            return False
        else:
            return True
