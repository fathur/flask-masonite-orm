from flask_restful import Resource, fields

from app.services import success

application_fields = {
    'id': fields.Integer,
    'ktp': fields.String(attribute='identity_number')
}


class ApplicationListResource(Resource):

    def get(self):
        from app.models import Application
        applications = Application.all().serialize()
        return success(data=applications, field=application_fields)


class ApplicationItemResource(Resource):
    def get(self, application_id):
        from app.models import Application
        application = Application.find(application_id)
        return success(data=application, field=application_fields)


class ApplicationListV2Resource(Resource):

    def get(self):
        from app.models import Application
        applications = Application.all().serialize()
        return success(data=applications, field=application_fields)
