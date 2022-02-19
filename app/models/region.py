""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many, belongs_to


class Region(Model):
    """Region Model"""

    @has_many
    def applications(self):
        from app.models import Application
        return Application
