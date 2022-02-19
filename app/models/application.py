""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class ApplicationRelations:
    @belongs_to
    def customer(self):
        from app.models import Customer
        return Customer

    @belongs_to
    def region(self):
        from app.models import Region
        return Region

    @belongs_to
    def status(self):
        from app.models import Status
        return Status


class ApplicationProperties:

    @property
    def readable_gender(self):
        switcher = {
            'M': 'Male',
            'F': 'Female'
        }

        return switcher.get(self.gender)

    @property
    def is_latest(self):
        return False


class ApplicationAction:

    def sync_to_customer(self):
        """

        :return:
        """
        customer = self.customer
        # todo some sync data process
        return customer.save()


class Application(
    Model,
    ApplicationRelations,
    ApplicationProperties,
):
    """Application Model"""
    pass

