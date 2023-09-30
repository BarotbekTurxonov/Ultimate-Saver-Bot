from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS
from loader import db

#Dasturchi @Mrgayratov kanla @Kingsofpy
class IsSuperAdmin(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id

        if str(user_id) in ADMINS:
            return True
        else:
            return False
#Dasturchi @Mrgayratov kanla @Kingsofpy
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        user_id = str(message.from_user.id)
        admin = db.is_admin(user_id=user_id)
        print(admin)
        if admin:
            return True
        else:
            return False
#Dasturchi @Mrgayratov kanla @Kingsofpy