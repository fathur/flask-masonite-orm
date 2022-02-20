from flask_restful import Resource, fields

from app.resources import application_fields
from app.services import Nested
from app.services import ok

customer_fields = {
    'id': fields.Integer,
    'applications': Nested(application_fields)
}


class CustomerItemResource(Resource):
    def get(self, customer_id):
        from app.models import Customer
        customer = Customer.with_('applications').find(customer_id)
        return ok(data=customer, field=customer_fields)
