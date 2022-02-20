from http import HTTPStatus


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
