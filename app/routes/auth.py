from app.resources.registration_resource import RegistrationResource


def routes(api):
    api.add_resource(RegistrationResource, '/auth/register')
