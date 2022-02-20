from flask_restful import marshal
from flask_restful.fields import get_value, Nested as NestedField
from http import HTTPStatus


class Nested(NestedField):

    def output(self, key, obj):
        value = get_value(key if self.attribute is None else self.attribute, obj)
        if value is None:
            if self.allow_null:
                return None
            elif self.default is not None:
                return self.default

        return marshal(value.serialize(), self.nested)


class Response:

    @staticmethod
    def _base_format(data, field: dict = None, links: dict = None) -> dict:
        from flask_restful import marshal
        if field is not None:
            data = marshal(data, field)

        return {
            'data': data,
            'links': links if links is not None else {},
            'meta': {}
        }

    @classmethod
    def success(cls, data, field=None, links=None):
        return cls._base_format(data, field, links), HTTPStatus.OK

    @classmethod
    def ok(cls, data, field=None, links=None):
        return success(data, field, links)

    @classmethod
    def created(cls, data, field=None, links=None):
        return cls._base_format(data, field, links), 201


def success(data, field=None, links=None):
    return Response.success(data, field, links)


def ok(data, field=None, links=None):
    return Response.ok(data, field, links)
