from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

from app.observers import ApplicationObserver
import json

from masoniteorm.scopes import UUIDPrimaryKeyMixin
from masoniteorm.relationships import has_many
from app.observers.user_observer import UserObserver


class Account(Model):
    pass


class Application(Model):
    @belongs_to
    def customer(self):
        return Customer

    @belongs_to
    def region(self):
        return Region

    @belongs_to
    def status(self):
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


class AuditLog(Model, UUIDPrimaryKeyMixin):
    __fillable__ = [
        'auditable', 'auditable_id', 'event',
        'old_values', 'new_values'
    ]

    @classmethod
    def audit_model(cls, model, event):
        original_attributes = model.__original_attributes__
        dirty_keys = model.get_dirty_keys()
        compact_original_attributes = dict()
        for (key, value) in original_attributes.items():
            if key in dirty_keys:
                compact_original_attributes[key] = value

        original_attributes = compact_original_attributes
        dirty_attributes = model.__dirty_attributes__

        if event == 'created':
            original_attributes = {}
            dirty_attributes = model.serialize()
        elif event == 'deleted':
            original_attributes = model.serialize()
            dirty_attributes = {}

        cls.create({
            'auditable': model.__class__.__name__,
            'auditable_id': model.id,
            'event': event,
            'old_values': json.dumps(original_attributes, default=str),
            'new_values': json.dumps(dirty_attributes, default=str)
        })


class User(Model):
    __table__ = 'users'


User.observe(UserObserver())


class Customer(User):
    @has_many('id', 'user_id')
    def applications(self):
        return Application

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Device(Model):
    pass


class ProductLine(Model):
    pass


class Region(Model):
    @has_many
    def applications(self):
        return Application


class Status(Model):
    @has_many
    def applications(self):
        return Application


class Workflow(Model):
    pass
