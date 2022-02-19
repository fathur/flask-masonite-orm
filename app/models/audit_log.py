""" User Model """
import json

from masoniteorm.models import Model
from masoniteorm.scopes import UUIDPrimaryKeyMixin


class AuditLog(Model, UUIDPrimaryKeyMixin):
    """AuditLog Model"""

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
