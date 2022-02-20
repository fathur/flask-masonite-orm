from app.resources import CustomerItemResource
from app.resources.application_resource import ApplicationListV2Resource, ApplicationListResource, \
    ApplicationItemResource


def routes(api):
    api.add_resource(ApplicationListResource, '/application-flow/applications')
    api.add_resource(ApplicationItemResource, '/application-flow/applications/<int:application_id>')
    api.add_resource(CustomerItemResource, '/application-flow/customers/<int:customer_id>')
