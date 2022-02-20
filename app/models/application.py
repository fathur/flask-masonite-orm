""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

from app.observers import ApplicationObserver


class Application(Model):
    """Application Model"""

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

    def sync_to_customer(self):
        """

        :return:
        """
        customer = self.customer
        # todo some sync data process
        return customer.save()

    def has_good_payment_history(self):
        return True

    def is_paid_on_time(self):
        return False


Application.observe(ApplicationObserver())
