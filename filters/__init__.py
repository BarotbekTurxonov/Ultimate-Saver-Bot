from aiogram import Dispatcher

from loader import dp
from .admins import IsSuperAdmin
from .users import IsUser, IsGuest

if __name__ == "filters":
    #Dasturchi @Mrgayratov kanla @Kingsofpy
    # dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsSuperAdmin)
    dp.filters_factory.bind(IsUser)
    dp.filters_factory.bind(IsGuest)
