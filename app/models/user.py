""" User Model """

from masoniteorm.models import Model


class User(Model):
    """User Model"""

    __table__ = 'users'
