""" User Model """

from masoniteorm.models import Model

from app.observers.user_observer import UserObserver


class User(Model):
    """User Model"""

    __table__ = 'users'


User.observe(UserObserver())
