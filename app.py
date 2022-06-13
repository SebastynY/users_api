from flask import Flask
from flask_restful import Api
from resources.user import UserListResource, UserResource, UserIdentificationResource

app = Flask(__name__)
api = Api(app)
api.add_resource(UserListResource, '/users/')
api.add_resource(UserResource, '/users/<string:user_id>')
api.add_resource(UserIdentificationResource, '/users/<string:user_id>/identification')

if __name__ == '__main__':
    app.run()
