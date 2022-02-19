""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Status(Model):
    """Status Model"""

    @has_many
    def applications(self):
        from app.models import Application
        return Application
