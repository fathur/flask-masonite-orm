""" User Model """

from masoniteorm.relationships import has_many

from app.models import User


class Customer(User):
    """Customer Model"""

    @has_many('id', 'user_id')
    def applications(self):
        from app.models import Application
        return Application

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


