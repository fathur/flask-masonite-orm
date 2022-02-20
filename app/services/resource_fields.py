from flask_restful import marshal
from flask_restful.fields import get_value, Nested as NestedField


class Nested(NestedField):

    def output(self, key, obj):
        value = get_value(key if self.attribute is None else self.attribute, obj)
        if value is None:
            if self.allow_null:
                return None
            elif self.default is not None:
                return self.default

        return marshal(value.serialize(), self.nested)
